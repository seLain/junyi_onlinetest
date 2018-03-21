
def exclude(n):
	counter = 0
	for i in range(1, n+1):
		if i%3 == 0 and i%5 == 0:
			counter += 1
		elif i%3 != 0 and i%5 != 0:
			counter += 1
	return counter
	