text = input()
count = 0
 
for i in range(len(text)//2):
    if text[i] != text[-1-i]:
        count += 1
 
if (count == 1) or (count == 0 and len(text)%2 != 0):
    print("YES")
else:
    print("NO")
