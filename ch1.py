# import re
# data = [
#     "john@ggmail.com",
#     "invalid-email",
#     "alice@yahoo.com",
#     "test@",
#     "bob@gmail.com"
# ]

# pattern = r'^[\w]+@[\w]+\.[A-Za-z]{2,}$'
# global count
# count = 0
# def validate():
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             print("Starting email validation...")
#             func(*args, **kwargs)
#             global count
#             count +=1
#             print("Email validation completed.")
            
#         return inner
#     return wrapper
    
# l = []
# @validate()
# def validate_email():
#     iterator = iter(data)

#     while True:
#         try:
#             email = next(iterator)
#             print(f"Validating email: {email}")
#             if re.findall(pattern, email):
#                 print(f"Valid email: {email}")
#                 if email.endswith("@gmail.com"):
#                     l.append(email)       
#             else:
#                 print(f"Invalid email: {email}")
#         except StopIteration:
#             break   

# validate_email()

# print("gamils are:"+str(l))
# print("total calls: " + str(count))     
import re
# students = [
#     ("BCA101", "Alice", 85),
#     ("BCA102", "Bob", 92),
#     ("BCA103", "Charlie", 78),
#     ("BCA104", "David", 90),
#     ("INVALID", "Eve", 88)
# ]
# global count
# count=0
# pattern = r'^BCA\d+$'
# def validate():
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             print("Starting student validation...")
#             func(*args, **kwargs)
#             print("Student validation completed.")
            
#         return inner
#     return wrapper

# @validate()
# def validate_students():
#     for student in students:
#         student_id, name, score = student
#         print(f"Validating student: {student_id}, {name}, {score}")
#         if re.match(pattern, student_id):
#             global count
#             count += 1
#             print(f"Valid student: {student_id}, {name}, {score}")
            
#         else:
#             print(f"Invalid student: {student_id}, {name}, {score}")

#     students.sort(key=lambda s: s[2])
#     print("Sorted scores: " + str([student for student in students]))

# validate_students()
# print("Total valid students: " + str(count))
books = ["python basics","java programming","python advance","c++ programming"]
def log(func):
    def wrapp():
        print("Starting book search...")
        func()
        print("Book search completed.")
    return wrapp
    

@log
def search():
    st = input("Enter the book name to search: ")
    pattern = r'(?i)'+re.escape(st)
    for book in books:
        if re.search(pattern, book):
            print(f"Book found: {book}")
    
search()