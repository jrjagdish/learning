from quiz_converter import convert_file_to_json

# Change this to your quiz file name (pdf or image)
file_path = "sample_quiz.pdf"  # or "quiz_image.jpg"

try:
    json_result = convert_file_to_json(file_path)
    print("\n✅ Quiz JSON Output:\n")
    print(json_result)
except Exception as e:
    print("❌ Error:", e)
