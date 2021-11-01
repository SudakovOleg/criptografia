def find_simple(last_num):	
	exclude_list = []
	simple_list = [i for i in range (2, last_num)]
	for i in simple_list:
		for j in simple_list:
			if not j%i and j != i:
				exclude_list.append(j)
				simple_list.remove(j)
	return simple_list
		
def diemitko(q):
    if not q%2 or not q in find_simple(1000):
        print("Введите нечетное, простое число")
        return
    simple_list = [ q*i+1 for i in range(2, 4*(q+1)) if not i%2 ]
    result_list = []
    for elm in simple_list:
            a = 0
            while(a < elm):
                if (pow(a, elm - 1)%elm == 1) and (pow(a, (elm - 1)/q)%elm != 1):
                        result_list.append(elm)
                        break
                a += 1
                
    return result_list
