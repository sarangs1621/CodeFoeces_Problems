n = int(input())
s = input()
c = 0
i = 0
while i<n-1:
    if s[i]!= s[i+1]:
        c = c+1
        i = i+2
    else:
        i = i+1
t = n-c
print(t)
