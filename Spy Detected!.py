for i in range(int(input())):
    input()
    d = input().split()
    print(d.index(min(d, key=d.count)) + 1)
