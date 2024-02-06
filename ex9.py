A = input()
B = A.split()
B = list(map(float,B))
sum = 0.0
for i in range (0,10):
	sum += B[i]
average = sum/10
print(f"{average:.6f}")