#methord 1
s = input()
t = input()
 
if len(s) != len(t):
    print("No")
else:
    for i in range(len(s)):
        ss = s[i] in "aiueo"
        tt = t[i] in "aiueo"
        if ss != tt:
            print("No")
            break
    else:
        print("Yes")
