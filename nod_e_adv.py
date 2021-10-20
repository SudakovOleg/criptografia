def nod_e_adv(a,b):
	x,y,last_x,last_y,r = 0,1,1,0,-1
	if b > a:
		a,b = b,a
	print ("Input: a = ", a, ", b = ", b)
	while r:
		print("New step: a = ", a, ", b = ", b)
		print("New step: x = ", x, ", y = ", y)
		tmp_x,tmp_y = x,y		
		r = a % b		
		x = last_x - a//b*x
		y = last_y - a//b*y		
		a,b = b,r
		last_x,last_y = tmp_x,tmp_y
	return last_x,last_y
