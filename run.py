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
#     for i in f:
#         print(i.strip())

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

# import sys

# try:
#     filename = sys.argv[1]
#     with open(filename,'r') as f:
#         print(f"File content: {f.read()}")

# except Exception as e:
#     print(f"error occured {e}")
