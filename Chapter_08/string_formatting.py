# Basic formatting
a = 10
b = 30
print("The values of a and b are %d %d" % (a, b))
c = a + b
print("The value of c is %d" % c)

str1 = 'John'
print("My name is %s" % str1)

x = 10.5
y = 33.5
z = x * y
print("The value of z is %f" % z)
print()

# aligning
name = 'Mary'
print("Normal: Hello, I am %s !!" % name)
print("Right aligned: Hello, I am %10s !!" % name)
print("Left aligned: Hello, I am %-10s !!" % name)
print()

# truncating
print("The truncated string is %.4s" % ('Examination'))
print()

# formatting placeholders
students = {'Name' : 'John', 'Address' : 'New York'}
print("Student details: Name:%(Name)s Address:%(Address)s" % students)

