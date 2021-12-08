#method 1
def berlanese(word):
    vowels = 'aeiou'
    n = len(word)
    for i in range(n):
        if word[i] not in vowels and word[i] != 'n':
            if i == n - 1 or word[i + 1] not in vowels:
                return 'NO'
    return 'YES'
 
s = input()
print (berlanese(s))

#method 2
text = input()
L = ['a', 'e', 'i', 'o', 'u', 'n']
M = ['a', 'e', 'i', 'o', 'u']
text = text + 'n'
a = True
for i in range(len(text)-1):
    if text[i] not in L and text[i+1] not in M:
        a = False
if a :
    print("YES")
else:
    print("NO")
