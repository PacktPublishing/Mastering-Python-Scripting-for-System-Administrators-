import re

print("str1:- ")
str1 = "Sky is blue. Sky is beautiful."
print("Original: ", str1)
p = re.subn('beautiful', 'stunning', str1)
print("Replaced: ", p)

print()
print("str_line:- ")
str_line = 'Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?'
print("Original: ", str_line)
p = re.subn('Peter', 'Mary', str_line)
print("Replaced: ", p)
