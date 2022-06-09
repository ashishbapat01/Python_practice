s={10, 20, 30}
print(s.pop())
print(s)

s={10, 20, 30, 40, 50}
print(s.remove(30))
print(s)

s={10, 20, 30}
s.clear()
print(s)

s={10, 20, 30}
s1={40, 50, 60}
print(s.union(s1))

s={10, 20, 30}
s1={40, 20, 60}
print(s.intersection(s1))

s={10, 20, 30}
s1={40, 50, 60}
print(s.difference(s1))

s= ' durga '
print(s)
print('d'in s)

s={x*x for x in range(5)}
print(s)

l=eval(input("enter the number :- "))
s=set(l)
print(s)

w=input("enter  word to search the vowels")

#accept list from user and count the frequency of all character present in string