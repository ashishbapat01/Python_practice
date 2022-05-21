!=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!==0,l))
print(l2)


!=[1,2,3,4,5]
l1=list(map ( X:2*X,l))
print(l1)

l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2 ))