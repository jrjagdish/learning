import os
import pytesseract
from PIL import Image
import pdfplumber
import openai
import google.generativeai as genai

# === Set your API keys here ===
openai.api_key = "YOUR_OPENAI_API_KEY"
genai.configure(api_key="YOUR_GEMINI_API_KEY")

USE_OPENAI = True  # Set False to use Google Gemini instead

# === For Windows users: set this if you use OCR on images ===
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def convert_to_json(text):
    prompt = f"""
You are an intelligent quiz parser.

The input text contains quiz content that may include:
- Chapter titles (optional)
- Questions with options (A, B, C, D)
- Answer keys and explanations, which may be at the end or after each question

Your task:
- Parse the quiz into a JSON object grouped by chapters.
- Each chapter should have a "chapter" field and a "questions" list.
- Each question must include: question text, options, correct_option (the letter), and explanation.
- If chapters are missing, assign the chapter name as "General".
- If answer or explanation is missing, leave them empty ("").

Return only valid JSON.

Example output format:

{{
  "chapters": [
    {{
      "chapter": "Chapter Title",
      "questions": [
        {{
          "question": "Question text here",
          "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
          "correct_option": "B",
          "explanation": "Explanation text here"
        }},
        ...
      ]
    }},
    ...
  ]
}}

Input quiz text:

{text}
"""

    if USE_OPENAI:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    else:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()

def convert_file_to_json(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file format! Use PDF or JPG/PNG image.")

    json_output = convert_to_json(text)
    return json_output
