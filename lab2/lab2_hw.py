from random import randint

number = int(input("Enter number of rows >>> "))
max_num_len = len(str(number))

# Length of any line is length of all numbers and (number - 1)
# spaces
line_len = (max_num_len * number) + (number - 1)

for i in range(number):
	# Generating separator of needed length for numbers of this line. Sep length
	# is length of largest number - length of current number + one space
	num_sep = " " * (max_num_len - len(str(i+1)) + 1)
	
	# Generating substring with spaces at the beginning of this line.
	# Substring length = string length - length of all numbers and separators
	# for this line.
	space_start = " " * (line_len - (len(str(i+1)) * (i+1) + (i * len(num_sep))))
	
	# Printing result
	print(space_start, end="")
	print(*([i+1] * (i+1)), sep=num_sep, end="\n")
	

#############################################################################

number = int(input("Enter number >>> "))
while number >= 10:
	number //= 10
	
print(number)

############################################################################

nums = []
number = ''

# User input and list generation
while number != 'c':
	number = input("Enter a number or 'c' to stop or 'r' to generate list >>> ")	
	if number == 'c':
		break	
	if number == 'r':
		list_len = int(input("How many numbers do you want to be in the list? >>> "))
		for i in range(list_len):
			nums.append(randint(-100, 100))
		break
	try:
		number = int(number)
		nums.append(number)	
	except:
		print("Not a number, try again!")
		
# Selection sort
for i in range(len(nums)):
	min_idx = i
	for j in range(i+1, len(nums)):
		if nums[min_idx] > nums[j]:
			min_idx = j

	nums[min_idx], nums[i] = nums[i], nums[min_idx]

print(*nums)
		
