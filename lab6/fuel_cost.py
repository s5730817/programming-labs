def fuel_cost(distance_miles):
#     # Constants
	MPG = 50  # Miles per gallon
	LITERS_PER_GALLON = 4.5
	PRICE_PER_LITER = 1.49  # Price in pounds per liter
	
	total_cost = (distance_miles / MPG) * LITERS_PER_GALLON * PRICE_PER_LITER
	
	return total_cost

while True:
	miles = int(input())
	print(fuel_cost(miles))
