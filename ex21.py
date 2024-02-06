s = int(input())
add = 0
for i in range(1,s+1):
	m = int(input())
	add = add + m
per = (add/(s*80))*100
print(f"{per:.2f}",end="%")