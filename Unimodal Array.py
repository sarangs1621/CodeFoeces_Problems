n=int(input())
arr=list(map(int,input().split()))
x=True
y=False
z=False
b=True
for i in range(1,n):
    if arr[i] <= arr[i-1] and x:
        x=False
        y=True
    if arr[i] != arr[i-1] and y:
        y=False
        z=True
    if arr[i] >= arr[i-1] and z:
        print('NO')
        b=False
        break
if b:
   print('YES')









































  
