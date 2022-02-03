n,m=map(int,input().split())
l=[]
total=count=0
for i in range(n):
    a,b=map(int,input().split())
    l.append(a-b)
    total+=a
l.sort(reverse=True)
while(total>m and count<=n):
    try:
        total-=l[count]
    except:
        count=-1
        break
    count+=1
print(count)
