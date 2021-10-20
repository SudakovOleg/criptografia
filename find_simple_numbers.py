def find_simple(last_num):	
	exclude_list = []
	simple_list = [i for i in range (2, last_num)]
	for i in simple_list:
		for j in simple_list:
			if not j%i and j != i:
				exclude_list.append(j)
				simple_list.remove(j)
	return simple_list
		
