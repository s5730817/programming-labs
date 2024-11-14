def annual_net_income(gross_salary):
    # complete your function implementation here...
	if gross_salary >= 45000:
		net_salary = gross_salary * (1 - 0.5)
	elif gross_salary >= 30000:
		net_salary = gross_salary * (1 - 0.3)
	else:
		net_salary = gross_salary * (1 - 0.15)
	return net_salary
