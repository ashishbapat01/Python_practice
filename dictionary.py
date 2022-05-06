rec={}
n=eval(input("Enter number of student: "))
i=1
while i<= n:
    name=input ("enter the student name:-")
    marks=input("Enter % of marks of student:-")
    rec[name]=marks
    i=i+1
    print("Name of student","\t""% of marks")
    for x in rec:
        print("\t", x, "\t\t",rec[x])

d={100:"durga", 200:"ravi", 300:"shiva"}
print(d.setdefault(400,"Ashish"))
print(d)

name = input("enter the number of student :-")
d={}
for i in range(n):
    name = input("enter the student name:-")
    marks = input("Enter % of marks of student:-")
    d[name]=marks
while True:
    name=input("enter the student name to get marks: ")
    marks=d.get(name,-1)
    if marks==-1:
        print("student not found")
    else:
         print("The marks of",name,"are",marks)
    option=input("Do u find another student marks[yes[no]")
    if option=="no":
        break



'''square={x:x*x for x in range(1,6)}
print(square)'''

