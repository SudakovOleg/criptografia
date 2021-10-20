def nod_e(a,b):
	r = -1
	if b > a:
		a,b = b,a
	print ("Input: a = ", a, ", b = ", b)
	while r:
		print("New step: a = ", a, ", b = ", b)
		r = a % b
		a,b = b,r
	return a
