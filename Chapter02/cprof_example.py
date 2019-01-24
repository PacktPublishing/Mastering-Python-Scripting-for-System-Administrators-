mul_value = 0 
def mul_numbers( num1, num2 ):
	mul_value = num1 * num2; 
	print ("Local Value: ", mul_value)
	return mul_value
mul_numbers( 58, 77 )
print ("Global Value: ", mul_value)

