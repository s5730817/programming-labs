
### I. COMPARISON OPERATORS ###

a = 11
b = 5

result = a >= b
type_result = type(result)
print(f"result = {result} and its type is {type_result}")
print("\n" + 35 * "#" + "\n")

### II. STRINGS ###

unit_name = "Programming"
print(unit_name)
print(unit_name[0], unit_name[3], unit_name[7])

greeting_string = "Welcome to Programming Unit! This is level 4 unit :)"
print(f"# 2: {greeting_string}")
print(f"# 3: {greeting_string[0]} {greeting_string[4]}")
print(f"# 4: {greeting_string[0:5]}")
print(f"# 5: {greeting_string[-1]}")
print(f"# 6: {greeting_string[-4:]}")
print("# 7: No, strings are immutable")
print("\n" + 35 * "#" + "\n")

### III. TYPE ###
values = [11, 11.0, "11", "11" + "11", "a", True, "False"]

for value in values:
	print(f"{value} is of type {type(value)}")
print("\n" + 35 * "#" + "\n")

### IV. CONVERSIONS ###

x = "Hello there"
y = 10
z = 5.5

print("# 1, 2, 3:", type(x), type(y), type(z))
result = y + z
print("# 4:", type(result))
result = y + int(z)
print("# 5:", type(result))
result = z + float(y)
print("# 6:", type(result))
print("# 7:", type(str(z)))
result = x + str(y) + str(z)
print(f"# 8: {result}: {type(result)}")
print("# 9: No, as they're different types")
