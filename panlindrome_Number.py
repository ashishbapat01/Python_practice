num =eval(input("Enter Any Number"))
temp = 0
rev = 0
rem =0

temp = num
while (num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if (temp == rev):
    print("Number Is Palindrome")
else:
    print("Number is not Palindrome")