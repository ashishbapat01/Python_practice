t1=(10,20,30,30)
t2=(40,50,60)
t3=t1+t2
print(t3)

print(t1*3)
print(t1)
print(t2)

print("Count of 30 is",t1.count(30))
print("Count of 20 is",t1.count(20))
print("\n____________________________________\n")
print("index 30 is",t1.index(30))
print("\n___________________________________\n")
print("minimum number in tuple is ",min(t1))
print("minimum number in tuple is ",min(t2))
print("\n___________________________________\n")
print("maximum number in tuple is ",max(t1))
print("maximum number in tuple is ",max(t2))
print("\n___________________________________\n")
t4=sorted(t1)
print(t4)
print("\n___________________________________\n")
t5=(20,10,19,51,26)
t6=sorted(t5,reverse=True)
print(t5)
print(t6)
print("\n___________________________________\n")
a=10
b=20
c=30
d=40            #paking_Tuple
t=a,b,c,d
print(t)
print(type(t))
print("\n___________________________________\n")
p,q,r,s=t
print(p)
print(q)       #unpacking_Tuple
print(r)
print(s)
print("\n___________________________________\n")
t7=(x**2 for x in range(1,6))
print(type(t7))
for i in t7:
    print (i)
