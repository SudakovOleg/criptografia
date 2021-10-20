def reverse_element(a, m):
	Zm = [i for i in range(0, m)]
	for elm in Zm:
		if (a*elm)%m == 1:
			return elm
