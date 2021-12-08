n = int(input())
l1 = list(map(int, input().split(' ')))
c = 0
a = 0
for i in l1:
    if i == -1:
        if c > 0:
            c -= 1
        else:
            a += 1
    else:
        c += i
print(a)
