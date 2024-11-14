# Instance variable  => object banane ke sath value badal de usko instance variable 
# static variable
# Local variable

# self current class ke current object ka refence hold karta hai 



# declaration on instance 
# inside class => with the help of self
#  outside class => with the help of object 

#  declearing insode the classs instance variale  
# class Student:
#     def __init__(self,name):        # inside constructor
#         self.name=name
#     def show(self,age):                   # inside instance method
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
# obj = Student("anurag")
# obj.show(45)
# obj.display()


# #  declearing outside  the classs instance variale  
# class Student:
#     def __init__(self,name):        # inside constructor
#         self.name=name
#     def show(self,age):                   # inside instance method
#         self.age=age
#     def display(self):
#         print("qualification:",self.quali)
#         print("name:",self.name)
#         print("age:",self.age)
# obj = Student("anurag")
# obj.show(45)
# obj.quali="BSC"
# obj.display()


# calling self inside and outside 
# class Student:
#     def __init__(self,name):        # inside constructor
#         self.name=name
#     def show(self):                   # inside instance method
#         self.age=78
#     def display(self):
#         print("qualification:",self.quali)
#         print("name:",self.name)
#         print("age:",self.age)
# obj = Student("anurag")
# obj.show()
# obj.quali="BSC"
# obj.display()
# print(obj.age)
# print(obj.name)
        