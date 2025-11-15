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