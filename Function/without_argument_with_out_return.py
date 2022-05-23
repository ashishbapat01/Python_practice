def add(x,y):
    return x+y , x-y

def evodd(n):
    if(n%2==0):

        print("Number is even")
    else:
         print("Numer Is Odd")
def diff(n):
    if(n==0):
        print("Zero  Number")
    elif(n>=0):
        print("positive Number")
    else:
        print("Negative Number")
a, b=eval(input("Enter Two Number:- "))
sum, dif =add(a,b)
print("sum=", sum)
evodd(sum)
print(dif)
