#single level inheritance 
# multilevel inheritance 
# multiple inheitance

# single level
# class A:
#     def home(self):
#         print("h.no=58 ")
#     def car (self):
#         print("verna")
# class B(A):
#     def mydata(self):        
#         print("mydetail")

# obj=B()
# obj.home()
# obj.car()
# obj.mydata()



# # multilevel level
# class A:
#     def home(self):
#         print("h.no=58 ")
#     def car (self):
#         print("verna")
# class B(A):
#     def mydata(self):        
#         print("mydetail")
# class C(B):
#     def new(self):
#         print("hiiiii.....")

# obj=C()
# obj.home()
# obj.car()
# obj.mydata()
# obj.new()



# multiple level
# class A:
#     def n1(self):
#         print("A class n1 ")
#     def car (self):
#         print("verna")
# class B:
#     def n1(self):        
#         print("B class n1")    # with the help of MRO (method resolution order ki help se  left to right check karta hai ) jis class me mil jaata hai wahi se retuen kar deta hai 
# class C(A,B):                   # MRO/defth first both are same
#     obj2=A()
#     def n1(self):
         
#         print("hiiiii.....")     # method overriding order 

# obj=C()
# obj.n1()
# obj.car()
# obj.new()

# =================================================
# class A:
#     def n1(self):
#         print("hi")
# class B(A):
    
#     def n1(self):
#         print("hello")
#         super().n1()         # isme super likhne se A class ki method  aa ja rhi hai jabki dono ka same naam hai Method overriding ko resolve karne ke loye super ka use karte hai 
        
# obj= B()
# obj.n1()







