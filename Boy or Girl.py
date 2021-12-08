#1
n = input()
length = len(set(n))
 
if length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

#2
t=input()
s=""
for i in t:
    if i not in s:
        s=s+i
if len(s)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
