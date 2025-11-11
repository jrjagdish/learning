# a = (1,2,[3,4])
# a[2].append(5)
# print(a)

# a= 5 // 3
# print(a)
# a = 5*2
# b = 5**2
# print(a)
# print(type(b))

# a = 4.555
# print(int(a))
# s = "hello"
# # print(s[::-1]) #The format is [start:end:step] where -1 as the step means "go backwards
# # print(s.title())
# # print(s + "world")
# print("world" in s)
# nums = [1,2,3,4]
# print(nums + [6])
# print(nums.pop(3))
# print(nums.sort())


# my_set = {(1, 2, 3), 4, 5}
# print(my_set)

# remove duplicates
# def remove_duplicates(seq):
#     seen = set()
#     results = []
#     for i in seq:
#         if i not in seen:
#             results.append(i)
#             seen.add(i)


#     return results

# a = [1,2,2,3,5,5,6,7,7,8,4,3,1,2,3,4,5,5,6,6,7,8,9,3,4,5,6,7,3]
# b= remove_duplicates(a)
# print(b)    

# a = [3,4,5,6,7,8]
# a.pop(4)
# print(a)    

#type conversion
# a = 123
# print(float(a))
# print(str(a))

# a = "hello"
# print(list(a))


# a = 5
# b = 2.0
# print(a/b)
# a=12345
# b=str(a)
# c = list(b)
# result = []
# for i in c:
#     x=int(i)
#     result.append(x)
    
   
# print(result)

# a=['1','2','3','4']
# results = []
# for i in a:
#     x = int(i)
#     results.append(x)

# print(results)


# import math
# print(abs(-10))
# print(round(3.6))
# print(pow(2,3))
# print(math.sqrt(16))
# print(math.factorial(4))
 
# text = "backend"
# text = "B" + text[1:]
# print(text)

# email = "jagdish@example.com"
# username = email[:email.index('@')]
# domain = email[7+1:email.index('.')]
# rest = email.index('@')
# print(username, domain)
# print(rest)
# import math
# number = int(input("enter a number to find out sqrt"))
# result = math.sqrt(number)
# print(math.floor(result)) # if needed int instead of float
# print(result)
# import math
# a = 3.14159
# print(round(a,2))

# a = "FAANG_BACKEND"
# result = a[a.index('_')+1:a.index('E')]
# print(result)


# a = "developer"
# print(a[::-1])
# a = "BACKEND_AI_SYSTEMS"
# result = a[8:10]
# results = a[a.index('_')+1:10] # another method
# print(result)
# print(results)

# age = int(input("enter your age"))
# if(age>18):
#     print("adult")
# elif(age<18):
#     result =str( 18 - age)
#     print("wait for" + result +"years to become adult")
# else:
#     print("you are adult now")        

# logged_in = True
# access_given = False

# if logged_in and access_given:
#     print("welcome")
# else:
#     print("denied")    

# user = "admin"
# logged_in = True

# if logged_in:
#     if user == "admin":
#         print("welcome admin")
#     else:
#         print("welcome user")
# else:
#     print("user not logged in")          
# status = "Adult" if age >= 18 else "Minor"
# print(status)
# username = "jagdish"
# password = "1234"

# userinput = input("enter user name= ")
# passwordinput = input("enter password= ")

# if username == userinput and password == passwordinput:
#     print("login successfull")
# else:
#     print("invalid cradentials")    
# number = int(input("enter a number"))
# result = "Even" if number%2 == 0 else "odd"
# print(result)
# number = int(input("enter a number "))
# if number>0:
#     print("positive")
# elif number<0:
#     print("negative")
# else:
#     print("zero")     
# num1 = int(input("enter first number ")) 
# num2 = int(input("enter second number ")) 
# if num1>num2:
#     print(f"biggest number is {num1}")
# else:
#     print(f"biggest number is {num2}")    
# marks = int(input("Enter your marks"))
# if marks>=90:
#     print("A")
# elif marks<=89 and marks>=75:
#     print("B")
# elif marks<=74 and marks>=50:
#     print("C")
# else:
#     print("F")            

# year = int(input("enter the year "))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("it is a leap year")
#         else:
#             print("it is not a leap year")
#     else:
#         print("it is a leap year")
# else:
#     print("it is not a leap year")     
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")
# for i in range(51):
#    if i == 37:
#     break 
#    print(i)

# for i in range(21):
#     if i%2 == 0:
#         print(i)
#     continue    
# users = ["sunil", "jagdish", "alex", "meena","error"]
# target = "error"
# for user in users:
#     if user == target:
#         continue
#     print(f"prossesing user {user}")

# def create_user():
#     pass

# for i in range(20):
#     for j in range(20):
#         product = i*j
#         if product>20:
#             break
#         print(product)
# person = {"name": 10, "role": 50, "exp": 2}
# prev_values = 0
# for key,values in person.items():
    
#     if values>prev_values:
#         prev_values = values
#         max_key = key

# print(prev_values,max_key)    
# for i in range(2, 10, 2):  # even numbers
#     print(i)
# for i in range(3):
#     for j in range(3):
#         print(f"({i},{j})", end=" ")
#     print()

# person = {"name": 10, "role": 50, "exp": 2}
# for index,(key,values) in enumerate(person.items()):
#     print(index,key,values)

# i=1
# while i <= 30 :
#     if i%2 ==0:
#         print(i)
#     i+=1    

# while True:
#     username= input("enter names ")
#     if username == "stop":
#         break

  
# a=[[1,2],[3,4],[5,6]]
# for i in a:
#     for j in i:
#         print(j)

# a ="FANNG"
# for index,value in enumerate(a):
#     print(index,value)

# user = {
#     "name": "Jagdish",
#     "age": 22,
#     "skills": {
#         "languages": ["Python", "C++", "SQL"],
#         "frameworks": ["FastAPI", "Django"]
#     }
# }
# for key,values in user.items():
#     print(key,values)
#     if isinstance(values,dict):
#       for keys,value in values.items():
#         print(keys,value)
#         if isinstance(value,list):
#            for languages in value:
#               print(languages)

# a=[1,2,3,4]
# print(a[:4])

# users = [
#     {"name": "Alice", "age": 25, "role": "dev"},
#     {"name": "Bob", "age": 30, "role": "tester"},
#     {"name": "Charlie", "age": 28, "role": "manager"}
# ]
# for user in users:
#     results=[]
#     if user['role'] == 'dev':
#         print(f"Developer Found:{user["name"]} ({user["age"]} years old)")
# def greet(name):
#     print(f"hello,good morning {name}")   

# greet("jagdish")     
# def sum(a,b):
#     return a+b

# result = sum(10,20)
# print(result)

# def square(num):
#     return num**2 # another method num*num

# result = square(10)
# print(result)
# def calculate_area(length,width):
#     return length*width

# area = calculate_area(10,20)
# print(area)
# def is_even(num):
#     return "True" if num%2 == 0 else "False"

# result = is_even(4)
# print(result)
# def factorial(num):
#       if num == 0:
#             return 1
#       else:
#             return num*factorial(num-1)
# # def factorial(num):
# #         result = 1
# #         for i in range(1,num+1):
# #             result *= i
# #         return result

# answer = factorial(5)   
# print(answer)   


# def greet_user(name, lang):
#     if lang.lower() == "eng":
#       text = "Good morning"
#     elif lang.lower() == "hin":
#       text = "shubh munjane"  
#     else:
#        return("select proper lang")  
    
#     return (f"{text} {name}")

# result = greet_user("jagdish","hin")
# print(result)