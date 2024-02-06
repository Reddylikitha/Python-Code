input_values = input()
principal, rate, time = map(float, input_values.split())
interest = (principal * rate * time) / 100
print(f"{interest:.6f}")