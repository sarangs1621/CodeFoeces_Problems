n = int(input())
s = 0
for i in range(2,n):
    if (((n - i) % i)==0):
        s+=1;
 
print(s+1)
