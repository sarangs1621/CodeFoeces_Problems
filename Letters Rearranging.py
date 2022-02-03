for i in range(int(input())):
	l=list(input())
	l.sort()
	if l[0]==l[-1]:
		print(-1)
	else:
		print("".join(l))
