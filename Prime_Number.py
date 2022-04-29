num=eval(input("Enter Any Number"))
cnt = 2
for i in range (2,num):
    if num % i == 0:
        cnt += 1
    else:
        pass

if cnt == 2 :
    print("Number is prime")
else:
    print("Number in not prime ")







