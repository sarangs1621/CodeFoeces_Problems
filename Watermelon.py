weight = int(input())
if weight < 1 or weight > 100:
   print("Invalid Input")
elif weight % 2 != 0:
   print("NO")
elif weight == 2:
   print("NO")
else:
   print("YES")
 
