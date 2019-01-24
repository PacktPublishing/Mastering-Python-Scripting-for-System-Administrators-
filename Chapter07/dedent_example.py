import textwrap

str1 = '''
	Hello Python World \tThis is Python 101
	Scripting language\n
	Python is an interpreted high-level programming language for general-purpose programming.
	'''
print("Original: \n", str1)
print()
t = textwrap.dedent(str1)
print("Dedented: \n", t)
