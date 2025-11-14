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
        
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    # 1. Initialize result array and pointers
    result = [0] * n  # Initialize result array of size n with zeros
    left = 0
    right = n - 1
    insert_pos = n - 1
    
    # 2. Write the while loop based on the logic above
    while left <= right:
        # Compare absolute values, which corresponds to the squared values
        left_result = nums[left]**2
        right_result = nums[right]**2
        if left_result > right_result:
            result[insert_pos] = left_result
            left += 1
            insert_pos -= 1
        elif right_result >left_result:
            result[insert_pos] = right_result
            right -= 1
            insert_pos -= 1 
        else:
            result[insert_pos] = left_result
            insert_pos -=1
            left +=1      
        # Finish the code block below
        # ... 

        
    return result
    
answer = sorted_squares([-4, -1, 0, 3, 10])   
print(answer) 
        
     
