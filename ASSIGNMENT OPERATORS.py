num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1
result_add = result
result_add += num2
result_subtract = result
result_subtract -= num2
result_multiply = result
result_multiply *= num2
result_divide = result
result_divide /= num2
result_modulus = result
result_modulus %= num2
result_exponentiation = result
result_exponentiation **= num2
result_floor_divide = result
result_floor_divide //= num2
print(f"{num1} += {num2} -> {result_add}")
print(f"{num1} -= {num2} -> {result_subtract}")
print(f"{num1} *= {num2} -> {result_multiply}")
print(f"{num1} /= {num2} -> {result_divide}")
print(f"{num1} %= {num2} -> {result_modulus}")
print(f"{num1} **= {num2} -> {result_exponentiation}")
print(f"{num1} //= {num2} -> {result_floor_divide}")
