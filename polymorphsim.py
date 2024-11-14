# polymorphism is that one thing having many forms like multiply string or number both we doing multiple but output is different


class First:
    def first(self):
        print("first")
class Second:
    def first(self):
        print("second")
class Third:
    def first(self):
        print("third")

def fun(obj):
    obj.first()
obj=Second()
fun(obj)