a = int(input())
b = input()
c = []
for i in range(a - 1):
    c.append(b[i] + b[i + 1])
d = 0
e = c[0]
for j in c:
    f = c.count(j)
    if f > d:
        d = f
        e = j
print(e)
