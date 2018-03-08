
def takeinput():
	print "Enter the number you'd like to test for even or odd"

	numb = input()
	return numb

def evenorodd(num):
	if num%2 == 0:
		return True
	else:
		return False
def print_result():
	numb = takeinput()
	if evenorodd(numb):
		print "The number you entered "+ str(numb) +" is even"
	else:
		print "The number you entered "+ str(numb) +" is odd"

print_result()



