# import random
# import string

# chars = " " +string.punctuation + string.digits +string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)
# # print(f"chars: {chars}")
# # print(f"key: {key}")

# #encrypt
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"Original message: {plain_text}")
# print(f"Encrypted message: {cipher_text}")    


# #DECRYPT
# cipher_text = input("Enter a message to decrypt: ")
# plain_text= ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"Encrypted message: {cipher_text}") 
# print(f"Original message: {plain_text}")

# class Agent:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
    
#     def process(self,prompt):
#         return (f"{self.name} is thinking... about {prompt} model name : {self.model}")

# agent1 = Agent("Agent1","Model1")
# agent2 = Agent("Agent2","Model2")
# print(agent1.process("hello"))
# class SecureConnection:
#     def __init__(self):
#         self._status = "disconnected" # Protected variable
        
#     @property
#     def status(self):
#         """The getter: allows reading the value."""
#         return self._status
        
#     @status.setter
#     def status(self, new_status):
#         """The setter: adds validation before changing the value."""
#         if new_status not in ["connected", "disconnected"]:
#             raise ValueError("Invalid status")
#         self._status = new_status

# conn = SecureConnection()
# conn.status = "connected"
# print(conn.status)       # Access like an attribute, not a function: "disconnected"
 

# class BaseWorker:
#     def __init__(self, task_id):
#         self.task_id = task_id

#     def log(self):
#         print(f"Logging task {self.task_id}")

# class AIWorker(BaseWorker):
#     def __init__(self, task_id, model):
#         super().__init__(task_id) # Call the parent's __init__
#         self.model = model        # Add child-specific data

# worker = AIWorker(101, "Llama-3")
# worker.log() # Inherited from BaseWorker

# from abc import ABC, abstractmethod

# class PaymentGateway(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass # This is just a contract. No implementation here.

# class StripePayment(PaymentGateway):
#     def process_payment(self, amount):
#         return f"Processing ${amount} via Stripe API"

# #gateway = PaymentGateway() # ERROR! Cannot instantiate abstract class
# gateway = StripePayment()    # Works! It fulfilled the contract.
# print(gateway.process_payment(100))

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
        
    def __add__(self, other):
        # Defines what happens when you use '+' between two Vectors
        print(self.x, self.y, other.x, other.y)
        return Vector(self.x + other.x, self.y + other.y)
        
    def __eq__(self, other):
        # Defines what makes two Vectors "equal"
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = Vector(2, 3)

print(v1)      # Triggers __str__: Vector(2, 3)
print(v1 + v2) # Triggers __add__: Vector(3, 7)
print(v1 == v3) # Triggers __eq__: True