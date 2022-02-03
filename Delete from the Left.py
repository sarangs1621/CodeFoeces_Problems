a=input()
b=input()
l=len(a)-1
m=len(b)-1
while l>=0 and m>=0 and a[l]==b[m]:
    l-=1
    m-=1
print(l+m+2)
