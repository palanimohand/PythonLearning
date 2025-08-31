class A:

    def __init__(self, a):
        print("param constructor",a)

    def __init__(self):
        print("default constructor")


    def method1(self):
        print("A method1")

class B(A):

    def method1(self):
        print("B method1")

    def method2(self, *args):
        print(args)

ob = B(10)
ob.method1()
ob.method2(10)
ob.method2("str")
ob.method2(10,"str")
