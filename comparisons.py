from nod_e import *
from reverse_element import *
from euler_function import *

def comparisons(a, b, m):
	if nod_e(a,m) == 1:
		reverse_a = reverse_element(a, m)
		a = (a * reverse_a)%m
		b = (b * reverse_a)%m
		if (a == 1):
			return b
	else:
		nod = nod_e(a,m)
		if b%nod == 0:
			a /= nod
			b /= nod
			m /= nod
			print(a,b,m)
			reverse_a = reverse_element(int(a), int(m))
			a = (a * reverse_a)%m
			b = (b * reverse_a)%m
			result = []
			for i in range(0,nod):
				result.append(b + m*i)
			return result
		else:
			return -1
			
			
def power_comparisons(a, b, m):
        new_m = euler_function(m)
        return comparisons(a, b, new_m)  
