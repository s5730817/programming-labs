def is_golden_number(n):
	for a in range(1, n//2):
		b = n - a
		if a * b == 1000:
			return True
	return False
