class C:
    def my_method(self):
        print("I am C")

    def meth2(self):
        print("meth2")

class D(C):
    def my_method(self):
        print("I am D")

    def meth3(self):
        print("meth3")





c= D()
c.my_method()
c.meth2()
c.meth3()