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
	
