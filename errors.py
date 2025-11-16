# # # class FileError(Exception):
# # #     pass

# # # class ConfigError(Exception):
# # #     pass


# # # class ValidationError(Exception):
# # #     pass
# # class User:
# #     def __init__(self, username: str, password):
# #         self.username = username
# #         self.__password = password

# #     def check_password(self, password) -> bool:
# #         return self.__password == password


# # class Auth:
# #     def __init__(self):
# #         self.users = []

# #     def if_user(self, username: str):
# #         for user in self.users:
# #             if user.username == username:
# #                 return user
# #             return None

# #     def Register(self, username: str, password):
# #         if self.if_user(username):
# #             raise ValueError("User Exists")
# #         new_user = User(username, password)
# #         self.users.append(new_user)
# #         return new_user

# #     def Login(self, username: str, password):

# #         user = self.if_user(username)
# #         if not user:
# #             raise ValueError("User doesn't exists")
# #         if not user.check_password(password):
# #             raise ValueError("Invalid password")
# #         return True


# # auth = Auth()

# # auth.Register("alice", "pass1")
# # try:
# #     auth.Login("alice", "pass1")
# #     print("Alice logged in OK")
# # except Exception as e:
# #     print("Auth error:", e)
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} ({self.age})"

#     def __repr__(self):
#         return f"User(name={self.name}, age={self.age})"

# u = User("Jagdish", 20)
# print(u)          # Calls __str__
# print(repr(u))    # Calls __repr__

# class Animal:
    
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")        

#     def sleep(self):
#         print(f"{self.name} is asleep")   

# class Dog(Animal):
#     def speak(self):
#         print("woof")

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     def speak(self):
#         print("chu chu")

# dog = Dog("scooby")
# cat = Cat("Meow")
# mouse = Mouse("Mice")

# print(mouse.name)
# print(mouse.is_alive)
# mouse.sleep()
# mouse.eat()
# mouse.speak()
        

# student1 = Student("Jagdish",30)
# student2 = Student("patrck",35) 
# student3 = Student("patick",65) 
# student4 = Student("patrick",25) 
# student5 = Student("patric",45) 

# print(f"Class includes {Student.num_students} students")

# class Prey:
#     def flee(self):
#         print("this animal is fleeing")

# c  
# def deco(f):
#     def wrapper():
#         return "Decorated"
#     return wrapper
# @deco
# def greet():
#     return "Hello"
# print(greet())
# class Outer:
#      val =10
#      class Outer:
#           val = 20
#           def show(self):
#                print(Outer.val)
# Outer.Outer().show()
# t=([],)
# t[0].append(10)
# print(t)


# class B(A):
#      def s(self):
#           print("B")

# A.s(B())            

# b = B()
# b.x = 2
# print(A.x, B.x , b.x)

# from abc import ABC,abstractmethod

# class Shape:

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius* self.radius   

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#     def area(self):
#         return self.side* self.side       

     

# class Triangle(Shape):
#     def __init__(self,base , height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5      

# shapes = [Circle(4),Square(5),Triangle(6,7)]

# for i in shapes:
#     print(f"{i.area()}cm^2")
 

# class Book:

#     def __init__(self,title,author,num_pages):
#         self.title =title
#         self.author = author
#         self.num_pages =num_pages

#     def __str__(self):
#         return f"{self.title} by {self.author}" 

#     def __eq__(self, value):
#         return self.title == value.title and self.author == value.author   
    
#     def __lt__(self,other):
#         return self.num_pages < other.num_pages
    
#     def __add__(self,other):
#         return self.num_pages + other.num_pages
    
#     def __contains__(self,keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem__(self,key):
#         if key == "title":
#             return self.title
# book1 = Book("The Rabbit","J.R.R",310)
# book2 = Book("Harry Potter","J.K",223)

# # print(book2)
# # print(book1 == book2)
# # print(book2<book1)
# # print(book1+book2)
# # print("Harry" in book2)
# print(book2['title'])
# class Rectangle:
#     def __init__(self,width,height):
#         self._width =width
#         self._height = height

#     @property
#     def width(self):
#         return f"{self._width}cm"
#     @property
#     def height(self):
#         return f"{self._height}cm"  

#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:    
#             print("width must be greater than zero") 

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:    
#             print("height must be greater than zero") 

#     @width.deleter
#     def width(self):
#         del self._width
#         print("width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("height has been deleted")    


# rectangle = Rectangle(3,4)
# rectangle.width = 34

# del rectangle.width
# del rectangle.height
#print(rectangle.width)
#print(rectangle.height)
# def add_sprinkles(func):
#     def wrapper(*args,**kwargs):
#         print("*you add sprinkles*")
#         func(*args,**kwargs)
#     return wrapper  

# def add_fudge(func):
#     def wrapper(*args,**kwargs):
#         print("you add fudge")
#         func(*args,**kwargs)
#     return wrapper      

# @add_sprinkles
# @add_fudge
# def get_icecream(flavor):
#     print(f"here is your ice cream {flavor}")

# get_icecream("vanilla")    

# import time
# import datetime

# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     is_running = True

#     while is_running:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)

#         if current_time == alarm_time:
#             print("WAKE UP!😒😒")
#             is_running = False

#         time.sleep(1)

# if __name__ == "__main__":
#     alarm_time = input("Enter alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code} ")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"{pokemon_info['name']}")