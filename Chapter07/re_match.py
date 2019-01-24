import re

str_line = "This is python tutorial. Do you enjoy learning python ?"

obj = re.match(r'(.*) enjoy (.*?) .*', str_line)

if obj:
	print(obj.groups())
