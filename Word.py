x=input()
u=0
v=0
for i in x:
    if i.islower():
        u=u+1
    elif i.isupper():
        v=v+1
if u>=v:
    print(x.lower())
else:
    print(x.upper())
