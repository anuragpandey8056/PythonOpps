# Encapsulation is that class usme pure variable bhi aa jati hai class ke ander methods bhi aa jati hai use encapsulation kkhate hai 
class Student:
    school="IEHE"                          #static variable
    def __init__(self,name):               #CONSTRUCTOR
        self.name=name                     #INSTANCE VARIABLE
    def new1(self):                        #INSTANCE METHOD
        Student.city="Bhopal"
        state="MP"                          #LOCAL VARIABLE
    @classmethod                            #CLASS METHOD
    def new2():
        cls.schoolcode=101
    @staticmethod                           #STATIC METHOD
    def new3():
        print("welcome")