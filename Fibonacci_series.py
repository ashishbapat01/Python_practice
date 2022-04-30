num =eval(input("Enter Any Number"))
n1 = 0
n2 = 1
fib = 0
for i in range(num):
    fib=fib+n1
    n1=n2
    n2=fib
print(fib)