#election
t=int(input())
for i in range(0,t):
    a,b,c=map(int,input().split())
    if a==b==c:
        A,B,C=1,1,1
    elif a>b and a>c:
        B=a-b+1
        C=a-c+1
        A=0
    elif b>a and b>c:
        A=b-a+1
        C=b-c+1
        B=0
    elif c>a and c>b:
        B=c-b+1
        A=c-a+1
        C=0
    elif a==b and a>c:
        A,B=1,1
        C=a-c+1
    elif a==c and a>b:
        A,C=1,1
        B=a-b+1
    elif b==c and b>a:
        B,C=1,1
        A=b-a+1
    print(A,B,C)
