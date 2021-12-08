def main(thomas) :
  r = 1 
  for i in range(n-1) :
    english, science, maths, social = map(int, input().split())
    other = english + science + maths + social
    if (other > thomas) : 
      r = r + 1    
  return r
 
n = int(input())
e,sc,m,ss = map(int, input().split())
 
thomas = e + sc + m + ss
r = main(thomas)
 
print(r)
