t = int(input())

for _ in range(t):
    num = int(input())
    summ = 0
    add = 0 
    while num > 0:
        add = num % 10
        summ = summ + add
        num = num // 10
    print(summ) 
    
