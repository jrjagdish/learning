# # import random
# # import string

# # chars = " " +string.punctuation + string.digits +string.ascii_letters
# # chars = list(chars)
# # key = chars.copy()

# # random.shuffle(key)
# # # print(f"chars: {chars}")
# # # print(f"key: {key}")

# # #encrypt
# # plain_text = input("Enter a message to encrypt: ")
# # cipher_text = ""

# # for letter in plain_text:
# #     index = chars.index(letter)
# #     cipher_text += key[index]

# # print(f"Original message: {plain_text}")
# # print(f"Encrypted message: {cipher_text}")    


# # #DECRYPT
# # cipher_text = input("Enter a message to decrypt: ")
# # plain_text= ""

# # for letter in cipher_text:
# #     index = key.index(letter)
# #     plain_text += chars[index]

# # print(f"Encrypted message: {cipher_text}") 
# # print(f"Original message: {plain_text}")

# # class Agent:
# #     def __init__(self,name,model):
# #         self.name = name
# #         self.model = model
    
# #     def process(self,prompt):
# #         return (f"{self.name} is thinking... about {prompt} model name : {self.model}")

# # agent1 = Agent("Agent1","Model1")
# # agent2 = Agent("Agent2","Model2")
# # print(agent1.process("hello"))
# # class SecureConnection:
# #     def __init__(self):
# #         self._status = "disconnected" # Protected variable
        
# #     @property
# #     def status(self):
# #         """The getter: allows reading the value."""
# #         return self._status
        
# #     @status.setter
# #     def status(self, new_status):
# #         """The setter: adds validation before changing the value."""
# #         if new_status not in ["connected", "disconnected"]:
# #             raise ValueError("Invalid status")
# #         self._status = new_status

# # conn = SecureConnection()
# # conn.status = "connected"
# # print(conn.status)       # Access like an attribute, not a function: "disconnected"
 

# # class BaseWorker:
# #     def __init__(self, task_id):
# #         self.task_id = task_id

# #     def log(self):
# #         print(f"Logging task {self.task_id}")

# # class AIWorker(BaseWorker):
# #     def __init__(self, task_id, model):
# #         super().__init__(task_id) # Call the parent's __init__
# #         self.model = model        # Add child-specific data

# # worker = AIWorker(101, "Llama-3")
# # worker.log() # Inherited from BaseWorker

# # from abc import ABC, abstractmethod

# # class PaymentGateway(ABC):
# #     @abstractmethod
# #     def process_payment(self, amount):
# #         pass # This is just a contract. No implementation here.

# # class StripePayment(PaymentGateway):
# #     def process_payment(self, amount):
# #         return f"Processing ${amount} via Stripe API"

# # #gateway = PaymentGateway() # ERROR! Cannot instantiate abstract class
# # gateway = StripePayment()    # Works! It fulfilled the contract.
# # print(gateway.process_payment(100))

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
        
#     def __add__(self, other):
#         # Defines what happens when you use '+' between two Vectors
#         print(self.x, self.y, other.x, other.y)
#         return Vector(self.x + other.x, self.y + other.y)
        
#     def __eq__(self, other):
#         # Defines what makes two Vectors "equal"
#         return self.x == other.x and self.y == other.y

# v1 = Vector(2, 3)
# v2 = Vector(1, 4)
# v3 = Vector(2, 3)

# print(v1)      # Triggers __str__: Vector(2, 3)
# print(v1 + v2) # Triggers __add__: Vector(3, 7)
# print(v1 == v3) # Triggers __eq__: True
# class Car:
#     # Class attribute (shared across all instances)
#     total_cars = 0
    
#     def __init__(self, brand, color):
#         # Instance attributes (unique to each object)
#         self.brand = brand
#         self.color = color
#         self.speed = 0
#         Car.total_cars += 1
    
#     def accelerate(self, amount):
#         """Instance method: operates on instance data"""
#         self.speed += amount
#         return f"{self.brand} accelerated to {self.speed} km/h"
    
#     @classmethod
#     def create_luxury_car(cls,brand):
#         """Class method: operates on class data"""
#         return cls(brand, "gold")
    
#     @staticmethod
#     def car_info():
#         """Static method: doesn't access instance/class data"""
#         return "This is a Car class"
    
#     def __repr__(self):
#         return f"Car({self.brand}, {self.color}, {self.speed}km/h)"

# # Usage
# car1 = Car("Tesla", "red")
# car2 = Car("BMW", "blue")

# print(car1.accelerate(100))  # Tesla accelerated to 100 km/h
# print(Car.total_cars)  # 2
# print(Car.create_luxury_car("Ferrari"))  # Car(Ferrari, gold, 0km/h)

# class Flyable:
#     def fly(self):
#         return "Flying"

# class Swimmable:
#     def swim(self):
#         return "Swimming"

# class Duck(Swimmable,Flyable):
#     def quack(self):
#         return "Quack!"

# # Method Resolution Order
# print(Duck.__mro__)
# # (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)

# duck = Duck()
# print(duck.swim())  # Swimming
# print(duck.quack())  # Quack!
# print(duck.fly())  # Flying


# from abc import ABC, abstractmethod
# from datetime import datetime, timedelta
# from dataclasses import dataclass

# @dataclass
# class Book:
#     title: str
#     author: str
#     isbn: str
#     publication_year: int

# class User(ABC):
#     def __init__(self, user_id, name):
#         self.user_id = user_id
#         self.name = name
#         self.__borrowed_books = []
    
#     @abstractmethod
#     def borrow_limit(self):
#         pass
    
#     def borrow_book(self, book):
#         if len(self.__borrowed_books) >= self.borrow_limit():
#             return f"Cannot borrow. Limit ({self.borrow_limit()}) reached"
#         self.__borrowed_books.append(book)
#         return f"{self.name} borrowed '{book.title}'"
    
#     def return_book(self, isbn):
#         for book in self.__borrowed_books:
#             if book.isbn == isbn:
#                 self.__borrowed_books.remove(book)
#                 return f"'{book.title}' returned successfully"
#         return "Book not found in your borrowed list"
    
#     def list_borrowed_books(self):
#         if not self.__borrowed_books:
#             return f"{self.name} has no borrowed books"
#         books = [f"- {b.title}" for b in self.__borrowed_books]
#         return f"{self.name}'s books:\n" + "\n".join(books)

# class Student(User):
#     def borrow_limit(self):
#         return 3

# class Faculty(User):
#     def borrow_limit(self):
#         return 10

# # Testing
# book1 = Book("Python Programming", "John Doe", "ISBN123", 2020)
# book2 = Book("Data Science", "Jane Smith", "ISBN456", 2021)

# student = Student(1, "Alice")
# faculty = Faculty(2, "Dr. Bob")

# print(student.borrow_book(book1))
# print(student.borrow_book(book2))
# print(student.list_borrowed_books())
# print(student.return_book("ISBN123"))

# import json
# from pathlib import Path

# # Writing JSON
# data = {
#     "users": [
#         {"id": 1, "name": "Alice", "email": "alice@example.com"},
#         {"id": 2, "name": "Bob", "email": "bob@example.com"}
#     ],
#     "total": 2,
#     "active": True
# }

# # Method 1: Using open()
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)

# # Method 2: Return JSON string
# json_string = json.dumps(data, indent=4)
# print(json_string)

# # Reading JSON
# # Method 1: From file
# with open("data.json", "r") as f:
#     loaded_data = json.load(f)

# # Method 2: From string
# loaded_from_string = json.loads(json_string)

# # Custom encoding/decoding
# from datetime import datetime

# class DateTimeEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         return super().default(obj)

# data_with_date = {
#     "created": datetime.now(),
#     "message": "Hello"
# }

# json_with_date = json.dumps(data_with_date, cls=DateTimeEncoder, indent=4)
# print(json_with_date)

# # Custom decoder
# def datetime_parser(dct):
#     for key, val in dct.items():
#         try:
#             dct[key] = datetime.fromisoformat(val)
#         except (ValueError, TypeError):
#             pass
#     return dct

# parsed = json.loads(json_with_date, object_hook=datetime_parser)
# print(parsed)

import csv
from pathlib import Path

# Writing CSV
headers = ["ID", "Name", "Email", "Age"]
rows = [
    [1, "Alice", "alice@example.com", 28],
    [2, "Bob", "bob@example.com", 35],
    [3, "Charlie", "charlie@example.com", 32]
]

# Method 1: DictWriter (recommended)
with open("users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for id, name, email, age in rows:
        writer.writerow({
            "ID": id,
            "Name": name,
            "Email": email,
            "Age": age
        })

# Method 2: writer (list-based)
with open("users_simple.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

# Reading CSV
# Method 1: DictReader (returns dictionaries)
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        # {'ID': '1', 'Name': 'Alice', 'Email': 'alice@example.com', 'Age': '28'}

# Method 2: reader (returns lists)
with open("users.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        print(row)

# Advanced: Filtering and transforming
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    # Filter and convert types
    adults = [
        {**row, "Age": int(row["Age"])}
        for row in reader
        if int(row["Age"]) >= 30
    ]
    print(adults)