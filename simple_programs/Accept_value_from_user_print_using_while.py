n=eval(input("Enter Any No:- "))
for i in range(1,n+1):
    if(i==5):
        break
    print(i)
   """
#n=eval(input("Enter Any No:- "))
for i in range(1,n+1):
    if(i%2==1):
        continue
    print(i)
"""
n=eval(input("Enter Any No:- "))
for i in range(1,n+1):
    if(i==5):
        break
    print(i)
else:
    print("Successfully itrated")