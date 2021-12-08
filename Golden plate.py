w,h,k=map(int,input().split())
a=0
b=0
while w>=3 and h>=3 and b!=k:
  a+=(2*(w+h)-4)
  w-=4
  h-=4
  b+=1
print(a)
