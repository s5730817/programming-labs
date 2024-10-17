from math import sqrt

def area_calculate(sides):
	a, b, c = [int(i) for i in sides]
	s = (a + b + c) / 2
	tr_area = sqrt(s * (s - a) * (s - b) * (s - c))
	return tr_area

def input_validate(sides):
	# IN   -> List of some values
	# FUNC -> Check all criterea for further calculations
	# OUT  -> False if list fails any of the criteria, 
	# otherwise True

	# Check if user enters more or less than 3 things
	if len(sides) != 3:
		print("Too many/not enough arguments, try again...")
		return False
	
	# Check if these 3 things are actual numbers
	try:
		a = int(sides[0])
		b = int(sides[1])
		c = int(sides[2])
	except ValueError:
		print("Values must be numbers, try again...")
		return False
	
	# Check triangle inequality theorem
	if (a + b <= c) or (a + c <= b) or (b + c <= a):
		print("Incorrect sides values, try again...")
		return False
	
	return True

def main():
	sides = input("Enter sides >>> ")
	while not input_validate(sides):
		sides = input("Enter sides >>> ")
	
	area_calculate(sides)