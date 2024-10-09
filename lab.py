from datetime import datetime

sum = 0

start = datetime.now()

for i in range(1, 1000):
	sum += i

result_time = datetime.now() - start

print(result_time.microseconds)
