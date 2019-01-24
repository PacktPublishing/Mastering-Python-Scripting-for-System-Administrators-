import textwrap

sample_string = '''Python is an interpreted high-level programming language for 
general-purpose programming. Created by Guido van Rossum and first released in 			1991, Python has a design philosophy that emphasizes code readability, 
notably using significant whitespace.'''

w = textwrap.wrap(text=sample_string, width=30) 
print(w)
