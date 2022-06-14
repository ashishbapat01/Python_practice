pqr = 123


class student:
    xyz = 3184
    ''' This is doc part '''

    def __init__(self, id=0, name="NULL", marks=0):
        self.id = id
        self.name = name
        self.marks = marks

    def display(self):
        print("id={} name={} marks={}".format(self.id, self.name, self.marks))

s1=student(1,"Ashish",99)
print(s1.__dict__)
s1.display()
print(s1.__dict__)
s1.pqr=1342
print(s1.__dict__)
