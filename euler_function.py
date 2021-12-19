from prime_factors import *

def euler_function(m):
	prime_factors = find_prime_factors(m)
	factors = []
	for elm in prime_factors.keys():
		factors.append(pow(elm, prime_factors[elm])-pow(elm, prime_factors[elm]-1))
	result = 1
	for elm in factors:
		result *= elm
	return result

def euler_function_main():
	m = int(input("Введите число M: "))
	result = euler_function(m)
	print("Результат решения задачи: ", result)
