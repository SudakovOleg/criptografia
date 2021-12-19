def reverse_element(a, m):
	Zm = [i for i in range(0, m)]
	for elm in Zm:
		if (a*elm)%m == 1:
			return elm

def reverse_element_main():
	a = int(input("Введите число A: "))
	m = int(input("Введите число M: "))
	result = reverse_element(a, m)
	print("Результат решения задачи: ", result)
