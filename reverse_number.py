def reverse_num(num):
	soln = 0
	elem = 0
	
	while num:
		elem = num%10
		soln = elem + soln*10
		num = num/10
		
		
	return soln

print reverse_num(1029)
