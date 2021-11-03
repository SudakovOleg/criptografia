from nod_e import *
from euler_function import *
from prime_factors import *

def a_mod_m (a, m):
	if nod_e(a,m) != 1:
		return
	k = 1	
	while k < 100:
		if (a ** k)%m == 1:
			return k
		k += 1

def first_root (m):
	p1 = euler_function(m)
	pk = find_prime_factors(p1)	
	a = 2
	print(p1,pk)	
	while a < 100 and nod_e(a,m) == 1:
		flag = False
		for p in pk.keys():
			if (a ** p)%m == 1:
				print(a,p,m)
				flag = True				
				break
		if flag:		
			a += 1
		else:
			return a
            
def reduced_deduction (a, m):
    deductions = []
    for i in range(0,m - 1):
            deductions.append((a**i)%m)
    return deductions
