#accept string from user and count the frequency of all character present in string
"""""
str= eval(input("Enter string here:- "))
count=0
for i in str:
    count=0
    for j in str:
        if str[i] == str[j]:
          count += 1
print(i,"no of frequency count")"""

n=input("string:- ")
freq={}
for i in n:
    if i in freq:
        freq[i]=freq[i]+1

    else:
        freq[i]=1
    print(freq)