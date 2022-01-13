n=int(input())
a=list(map(int,input().split()))
if (a.count(0)==n):
  print('NO')
else:
  print('YES')
x=sum(a)
if x!=0:
  print(1)
  print(1,n)
else:
  for i in range(n):
    x=a[i]
    if x!=0:
      print(2)
      print(1,i+1)
      print(i+2,n)
      break
