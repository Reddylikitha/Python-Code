a = int(input())
reversed_number = 0

while a > 0:
    digit = a % 10
    reversed_number = reversed_number * 10 + digit
    a = a // 10

print(reversed_number)