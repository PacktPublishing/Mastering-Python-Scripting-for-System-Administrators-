import zipfile

for f_name in ['hello.py', 'work.zip', 'welcome.py', 'sample.txt', 'test.zip']:
	try:
		print('{:}	{}'.format(f_name, zipfile.is_zipfile(f_name)))
	except IOError as err:
		print('{:}	{}'.format(f_name, err))

