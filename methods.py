# instance method
# class method
# staticmethod 

class Empolyee:

    def __init__(self,name):
        self.name=name
    def newnew(self):
          print(self.subject5)
    @classmethod
    def new1(cls):
        Empolyee.subject1="sanskrit"
        x=10
        print("x is local=",x)
        print(Empolyee.subject6)
    @staticmethod
    def new2():
        Empolyee.subject5="hindi"
        print("thanku and welcome")
obj = Empolyee("anurag")
Empolyee.subject6="sst"
obj.new1()
obj.new2()
print(obj.subject1)
print(obj.subject5)
obj.subject5="english"

obj.newnew()
    