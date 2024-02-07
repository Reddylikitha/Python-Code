'''print("Hello World!")
x = 4
y = 5
print(id(x))
print(id(y))
print(type(x))
a = "likitha"
print(a)
print(type(a))

B = input()
print(type(B))
C = int(B)
print(C)

a = 7.5
b = int(a)
print(type(b))

b =7
a = float(b)
print(type(a))
print(a) 

print("likitha" ,"Sai" ,7,3,sep="--",end=":")
print("Love" , "date" ,sep=" ")'''

#a=5
#a/=3
#print(a)

# age = 18
# if age>18:
#  print("can vote")
# else:
#  print("Cannot vote")

# b = 13.6768
# c = 8.654
# d = b*c
# print(f"{d:.9f}")

'''A = input()
B = A.split()
print(B)'''

# a = 345
# a =  a//4
# print(a)

t = int(input())
for i in range(1,t+1):
	a = input()
	b=''
	for j in range(len(a)-1,-1,-1):
		b = a[j]
	print(b)