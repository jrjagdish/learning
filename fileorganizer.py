# from pathlib import Path
# import shutil
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# class FileOrganizer:
#     def __init__(self, extensions_map):
#         self.extensions = extensions_map
#         self.organized_count = 0
#         logging.info("FileOrganizer initialized")
    
#     def get_category(self, ext):
#         # Your code here
#         for category,cat_list in self.extensions.items():
#             if ext in cat_list:
#                 return category
#         return "others"
        
    
#     def scan_files(self, path):
#         # Your code here
#         folder = Path(path)
#         if not folder.exists():
#             logging.error(f"Path {path} does not exist.")
#             return []
#         if not folder.is_dir():
#             logging.error(f"Path {path} is not a directory.")
#             return []
#         return [file for file in folder.iterdir() if file.is_file()]
    
#     def organize_files(self, source_path, dest_path):
#         # Your code here
#         # Remember: self.organized_count += 1 after each file move
#         folder = Path(dest_path)
#         if not folder.exists():
#             logging.error(f"Destination path {dest_path} does not exist.")
#             return []
#         if not folder.is_dir():
#             logging.error(f"Destination path {dest_path} is not a directory.")
#             return []
#         folder.mkdir(parents=True, exist_ok=True)
#         logging.info(f"Created destination folder: {dest_path}")
#         files = self.scan_files(source_path)
#         if not files:
#             logging.info(f"No files to organize in {source_path}.")
#             return []
#         try:
#             for file in files:
#                 category = self.get_category(file.suffix.lower())
#                 category_folder = folder / category
#                 category_folder.mkdir(parents=True,exist_ok=True)
#                 logging.info(f"Moving {file} to {category_folder}")
#                 shutil.move(str(file), str(category_folder / file.name))
#                 self.organized_count += 1
#         except PermissionError as e:
#             logging.error(f"Permission error: {e}")
#         except Exception as e:
#             logging.error(f"An error occurred: {e}")
    
#     def get_summary(self):
#         # Your code here
#         # Return: "Organized {self.organized_count} files"
#         return f"Organized {self.organized_count} files"


# def main():
#     extensions_map = {
#         "images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
#         "documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
#         "videos": ['.mp4', '.avi', '.mkv', '.mov'],
#     }
    
#     organizer = FileOrganizer(extensions_map)
    
#     source = input("Enter source path: ")
#     dest = input("Enter destination path: ")
    
#     organizer.organize_files(source, dest)
#     print(organizer.get_summary())


# if __name__ == "__main__":
#     main()

# import errors
# # print(dir(errors))
# print(errors.__file__)
# print(errors.__name__)
# print(errors.__package__)
# print(errors.__builtins__)
# print(errors.__cached__)
# print(errors.__loader__)
# print(errors.__spec__)
# print(errors.__doc__)

# def outer_function(message):
#     def inner_function():
#         print(f"Message from closure: {message}")
#     return inner_function

# closure_function = outer_function("Hello, closures!")
# closure_function()
# # Output: Message from closure: Hello, closures!
# def simple_decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper

# @simple_decorator
# def greet():
#     print("Hello!")

# greet()
# Output:
# Before the function call
# Hello!
# After the function call

# def upper_case(function):
#     def wapper():
#         func = function()
#         mess = func.upper()
#         print(mess)
#         return mess
#     return wapper

# @upper_case
# def say():
#      return "hello world"

# say()
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""

#     def __init__(self, max=0):
#         self.max = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration


# # create an object
# numbers = PowTwo(3)

# # create an iterable from the object
# i = iter(numbers)

# # Using next to get to the next iterator element
# print(next(i)) # prints 1
# print(next(i)) # prints 2
# print(next(i)) # prints 4
# print(next(i)) # prints 8
# print(next(i)) # raises StopIteration exception

st  = "Hello world how are you"
count = 0

a=['a','e','i','o','u']
for i ,s in enumerate(st):
    if s in a:
        count+=1

print(count)
print(list(s))