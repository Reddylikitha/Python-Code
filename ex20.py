a = int(input())
for i in range(1,a+1):
	b = int(input())
	n = []
	for j in range(1,b+1):
		if j%3 != 0:
			n.append(str(j))
	print(' '.join(n))