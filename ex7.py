line = input()
B = line.split()
c = int(B[0])
d = int(B[1])
volume = 3.14*c*c*d
lit = volume/1000
cost = lit*40
print(f"{cost:.2f}")