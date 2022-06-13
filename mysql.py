num=eval(input("Enter Any Number"))
cnt=2
for i in range(2,num):
   if num % i==0:
     cnt+=1
   else:
     pass
if cnt == 2:
   print("Number Is Prime Number ")
else:
   print ("Number is Not Prime Number")