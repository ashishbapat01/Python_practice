class A:
    def fun(self):
        print("Am in A fun")

class B:
    def gun(self):
        print("Am in B gun")

class C(A,B):
    def run(self):
        print("Am in C run")

a=A()
a.fun()
b=B()
b.gun()
c=C()
c.fun()