def find_maximum_difference(a, b):
	maximum = max(max(a) - min(b), max(b) - min(a))
	return maximum

