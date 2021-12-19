def nod_e(a,b):
	r = -1
	if b > a:
		a,b = b,a
	print ("Входные значения: a = ", a, ", b = ", b)
	while r:
		print("Новый шаг: a = ", a, ", b = ", b)
		r = a % b
		a,b = b,r
	return a

def nod_e_main():
	a = int(input("Пожалуйста введите значение A: "))
	b = int(input("Пожалуйста введите значение B: "))
	result = nod_e(a,b)
	print("Результат решения задачи: ", result)

