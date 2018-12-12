import re

pattern = ['programming', 'hello']
str_line = 'Python programming is fun'

for p in pattern:
	print("Searching for %s in %s" % (p, str_line))

	if re.search(p, str_line):
		print("Match found")
	else:
		print("No match found")
