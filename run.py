# from quiz_converter import convert_file_to_json

# # Change this to your quiz file name (pdf or image)
# file_path = "sample_quiz.pdf"  # or "quiz_image.jpg"

# try:
#     json_result = convert_file_to_json(file_path)
#     print("\n✅ Quiz JSON Output:\n")
#     print(json_result)
# except Exception as e:
#     print("❌ Error:", e)

# FILE HANDLING

# lines = ["Jagdish\n", "Backend\n", "Developer\n"]

# with open('students.txt','w') as f:
#     f.writelines(lines)

# with open('students.txt','r') as f:
#     print(f.readline().strip())
#     print(f.read())

# import json


# data = {
#     "name": "Jagdish",
#     "skills": ["Python", "FastAPI"],
#     "experience": 1
# }

# with open('user.json' , 'w') as f:
#     json.dump(data,f,indent=4)

# with open('user.json' , 'r') as f:
#     content = json.load(f)
#     print(content['skills'])

# import csv

# with open("student.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "age", "role"])
#     writer.writerows([["Jagdish", 22, "Backend Dev"], ["Sunil", 23, "Frontend Dev"]])


# with open("student.csv" , 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# import os,shutil

# os.rename('student.csv' , 'roles.csv')
# shutil.copy('roles.csv' , 'bag.csv')

# import sys,os

# try:
#     filename = sys.argv[1]
#     if os.path.exists(filename):
#         with open(filename,'r') as f:
#             print(f"File content: {f.read()}")
#     else:
#         raise FileNotFoundError("File doesn't exists")   
# except IndexError :
#     print("please give file name")         


# import os
# with open('new.txt','w') as f:
#     f.write("This is the first line")
   
# def truncate_files(filename , no_of_bytes):

#   with open(filename,'rb+') as f:
#     f.seek(0,os.SEEK_END)
#     current_size = f.tell()
#     new_size = current_size - no_of_bytes
#     f.seek(new_size)
#     f.truncate()
#     f.seek(0)
#     print(f"Reading from second file: {f.read()}")
# import os

# def truncate_file_alt3(filename, n):
#     size = os.stat(filename).st_size
#     new_size = max(size - n, 0)

#     with open(filename, "rb+") as f:
#         f.truncate(new_size)
#         print(f.read())



# truncate_file_alt3('new.txt' , 10)


# import json

# data = {"db": "Postgres", "user": "admin", "password": "root"}

# with open('config.json' , 'w') as f:
#     json.dump(data,f,indent=4)

# with open('config.json' , 'r') as f:
#     content = json.load(f)
#     print(f"DB name is {content['db']}")  

# lines = ["Jagdish\n", "Backend\n", "Developer\n","helper\n","coder\n"]
# with open('first.txt','w') as f:
#     f.writelines(lines)
    
# with open('first.txt','r') as f:
#     f.readline()
#     count = f.tell()
#     f.seek(count)
#     s1 = f.readline()
#     s2 = f.readline()
#     print(s1,s2)

# a = [1,2,3,4,4,4,5,6,7,7,7,8,8,8,8]
# result = set()
# for i in a:
#     if i not in result:
#         result.add(i)
    
# print(result)    
        
# def sorted_squares(nums: list[int]) -> list[int]:
#     n = len(nums)
#     # 1. Initialize result array and pointers
#     result = [0] * n  # Initialize result array of size n with zeros
#     left = 0
#     right = n - 1
#     insert_pos = n - 1
    
#     # 2. Write the while loop based on the logic above
#     while left <= right:
#         # Compare absolute values, which corresponds to the squared values
#         left_result = nums[left]**2
#         right_result = nums[right]**2
#         if left_result > right_result:
#             result[insert_pos] = left_result
#             left += 1
#             insert_pos -= 1
#         elif right_result >left_result:
#             result[insert_pos] = right_result
#             right -= 1
#             insert_pos -= 1 
#         else:
#             result[insert_pos] = left_result
#             insert_pos -=1
#             left +=1      
#         # Finish the code block below
#         # ... 

        
#     return result
    
# answer = sorted_squares([-4, -1, 0, 3, 10])   
# print(answer) 
        
     
# import json
# import csv
# from pathlib import Path

# class DataConverter:
#     @staticmethod
#     def json_to_csv(json_file, csv_file):
#         """Convert JSON array to CSV"""
#         with open(json_file, "r") as f:
#             data = json.load(f)
        
#         if not data:
#             return
        
#         headers = data[0].keys()
#         with open(csv_file, "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=headers)
#             writer.writeheader()
#             writer.writerows(data)
#         print(f"Converted {json_file} to {csv_file}")
    
#     @staticmethod
#     def csv_to_json(csv_file, json_file):
#         """Convert CSV to JSON"""
#         with open(csv_file, "r") as f:
#             reader = csv.DictReader(f)
#             data = list(reader)
        
#         with open(json_file, "w") as f:
#             json.dump(data, f, indent=4)
#         print(f"Converted {csv_file} to {json_file}")

# # Test
# if __name__ == "__main__":
#     # Create test data
#     test_data = [
#         {"name": "Alice", "age": 28, "city": "NYC"},
#         {"name": "Bob", "age": 35, "city": "LA"},
#         {"name": "Charlie", "age": 32, "city": "Chicago"}
#     ]
    
#     with open("test.json", "w") as f:
#         json.dump(test_data, f, indent=4)
    
#     converter = DataConverter()
#     converter.json_to_csv("test.json", "test.csv")
#     converter.csv_to_json("test.csv", "converted.json")
# import timeit

# # Method 1: List comprehension
# lc = lambda: [x**2 for x in range(1000)]
# print(timeit.timeit(lc, number=10000))

# # Method 2: Loop
# def loop_version():
#     result = []
#     for x in range(1000):
#         result.append(x**2)
#     return result

# print(timeit.timeit(loop_version, number=10000))

# Task: Parse log data and extract statistics
# import re
# from datetime import datetime

# log_data = """
# 2024-01-01 10:30:45 ERROR Database connection failed
# 2024-01-01 10:31:02 INFO User login successful
# 2024-01-01 10:31:15 WARNING Memory usage high
# 2024-01-01 10:31:45 ERROR File not found
# 2024-01-01 10:32:10 INFO Data exported
# """

# # Parse logs using list comprehension
# pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"
# logs = [
#     {
#         "timestamp": match.group(1),
#         "level": match.group(2),
#         "message": match.group(3)
#     }
#     for line in log_data.strip().split("\n")
#     if (match := re.match(pattern, line))
# ]

# # Filter errors
# errors = [log for log in logs if log["level"] == "ERROR"]
# print(f"Found {len(errors)} errors:")
# for error in errors:
#     print(f"  - {error['timestamp']}: {error['message']}")

# # Count by level
# level_counts = {level: len([l for l in logs if l["level"] == level])
#                 for level in set(log["level"] for log in logs)}
# print(f"\nLog levels: {level_counts}")

# Similar to list comprehension but uses ()
# squares_gen = (x**2 for x in range(10))
# print(squares_gen)  # <generator object <genexpr> at 0x...>

# # Lazy evaluation - compute on demand
# print(next(squares_gen))  # 0
# print(next(squares_gen))  # 1

# # Can iterate through it
# for square in (x**2 for x in range(5)):
#     print(square)

# # Memory efficient for large data
# import sys

# # List: loads everything in memory
# big_list = [x**2 for x in range(1000000)]
# print(f"List size: {sys.getsizeof(big_list)} bytes")

# # Generator: minimal memory
# big_gen = (x**2 for x in range(1000000))
# print(f"Generator size: {sys.getsizeof(big_gen)} bytes")

# # With conditions
# even_squares = (x**2 for x in range(100) if x % 2 == 0)
# print(list(even_squares))
# def func(length):
#     for i in range(length):
#         yield i**2

# squares = func(10)
# for square in squares:
#     print(square)

# from openai import OpenAI

# client = OpenAI(
#     base_url="https://integrate.api.nvidia.com/v1",
#     api_key=""
# )

# with client.audio.speech.with_streaming_response.create(
#     model="nvidia/magpie-tts-multilingual",
#     voice="Magpie-Multilingual.EN-US.Aria",
#     input="Hello Jagdish, this is NVIDIA TTS.",
#     response_format="wav"
# ) as response:
    
#     response.stream_to_file("output.wav")

# print("Saved output.wav")

from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=""
)

PROMPT = """
Generate a complete executable Python project.

Requirements:
- Use MoviePy, PIL, and NumPy
- Do NOT use Manim
- Create smooth educational animations
- Teach Python basics visually
- Use cinematic transitions
- Animated text effects
- Code highlighting effects
- Modular clean code
- Production-style structure
- Output ONLY Python code
- No markdown
"""

completion = client.chat.completions.create(
    model="qwen/qwen3-coder-480b-a35b-instruct",

    messages=[
        {
            "role": "user",
            "content": PROMPT
        }
    ],

    temperature=0.7,
    top_p=0.8,
    max_tokens=8192,
    stream=True
)

# Stream directly to file (memory efficient)
with open("generated_video.py", "w", encoding="utf-8") as f:

    for chunk in completion:

        if not chunk.choices:
            continue

        content = chunk.choices[0].delta.content

        if content:
            f.write(content)
            f.flush()

print("Code saved to generated_video.py") 


