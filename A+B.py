#A+B (Trial Problem)
test_cases = int(input( )) #enter no. of test cases t(1≤t≤10^4)
for test_cases in range(test_cases):
    a,b = map(eval,input( ).split()) #enter a and b (−1000≤a,b≤1000)
    s = a + b
    print(s)


