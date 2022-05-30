L1 = []
L2 = []
count = 0
n=(int)(input("How Many element Do you want in List:-"))

for i in range(n):
    L1.append(input())

for i in L1:
    if i not in L2:
        count += 1
        L2.append(i)

print(count)

print(L2)
