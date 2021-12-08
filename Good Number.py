n,s=map(int,input().split())
u=0
for i in range(n):
    c=0
    x=input()
    for i in range(s+1):
        if str(i) in x:
            c=c+1
    if c==s+1:
        u=u+1
print(u)
