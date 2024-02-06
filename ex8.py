a=int(input())
b=list(map(int,input().split()))
c=max(b)
if c%2:
	print("LOST")
else:
	print("WON")