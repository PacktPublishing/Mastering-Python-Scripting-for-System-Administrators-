import tarfile

for f_name in ['hello.py', 'work.tar.gz', 'welcome.py', 'nofile.tar', 'sample.tar.xz']:
	try:
		print('{:}	{}'.format(f_name, tarfile.is_tarfile(f_name)))
	except IOError as err:
		print('{:}	{}'.format(f_name, err))
