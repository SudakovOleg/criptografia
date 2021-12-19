def nod_e_adv(a,b):
	x,y,last_x,last_y,r = 0,1,1,0,-1
	if b > a:
		a,b = b,a
	print ("Входные значения: a = ", a, ", b = ", b)
	while r:
		print("Новый шаг: a = ", a, ", b = ", b," | x = ", x, ", y = ", y)
		tmp_x,tmp_y = x,y		
		r = a % b		
		x = last_x - a//b*x
		y = last_y - a//b*y		
		a,b = b,r
		last_x,last_y = tmp_x,tmp_y
	return last_x,last_y

def nod_e_adv_main():
	a = int(input("Пожалуйста введите значение A: "))
	b = int(input("Пожалуйста введите значение B: "))
	result = nod_e_adv(a,b)
	print("Результат решения задачи: ", result)

