from nod_e import *
from reverse_element import *

def chinese_theorem(list_b, list_m):
	for elm1 in list_m:		
		for elm2 in list_m:
			if elm1 != elm2 and nod_e(elm1, elm2) != 1:
				return
	M = 1
	for elm in list_m:
		M *= elm
	
	x = 0
	for i in range(0, len(list_m)):
		rev = reverse_element(M/list_m[i], list_m[i])
		print(rev)
		tmp = list_b[i] * M/list_m[i] * rev
		print(tmp)
		x += tmp
	return x%M
		
