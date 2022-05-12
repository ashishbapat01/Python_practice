pqr=123
class student:
    xyz=3184
    ''' This is doc part '''

    def __init__(self,id=0,name="NULL",marks=0):
        self.id=id
        self.name=name
        self.marks=marks

    def display(self):
        print("id={} name={} marks={}".format(self.id,self.name,self.marks ))


s1=student(1,"kdn",99)
s1.display()
s2=student()
s2.display()
s1.xyz+=20
print(s2.xyz)
print(student.xyz)
print(student.xyz)
print(pqr)
