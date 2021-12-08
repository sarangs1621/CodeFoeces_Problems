#1
n = int(input())
count = 0
while(n>0):
    n-=1
    k = input()
    if k.count('1') >= 2:
        count+=1
print (count)

#2
n = int(input())
count = 0
for i in range(n):
    a, b, c = map(int, input().split(' '))
    if a + b + c >= 2:
        count += 1
print(count)
