n=int(input())
s=list(map(int,input().split()))
s.sort()
print(min(s[n-2]-s[0],s[n-1]-s[1]))
