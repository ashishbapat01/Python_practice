    class Test:
        a=10
        def __init__ (self):
            Test.b=20
        def m1(self):
            Test.c = 20

        @classmethod
        def m2(cls):
            cls.d1=40
            Test.d2=400

        @staticmethod
        def m3():
            Test.e=50

print(Test.dict )
t=Test()
print(Test.dict )
t.m1()
print(Test.dict )
Test.m2()
print(Test.dict )
Test.m3()
print(Test.dict )
Test.f=60
print(Test. dict )