a = 35
b = 57
try:
	c = a + b
	print("The value of c is: ", c)
	d = b / 0
	print("The value of d is: ", d)

except:
	print("Division by zero is not possible")

print("Out of try...except block")


