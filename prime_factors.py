from find_simple_numbers import *

def find_prime_factors(num):
	simple_nums = find_simple(120)
	result = {}
	for i in simple_nums:
		count = 0
		while not num%i:
			num /= i
			count += 1
		if count:		
			result[i] = count
	return result


def find_prime_factors_main():
	num = int(input("Введите число для разложения на множетели: "))
	result = find_prime_factors(num)
	print("Результат решения задачи: ", result)
