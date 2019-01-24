import os
directory_name = 'abcd'
print('Creating', directory_name)
os.makedirs(directory_name)
file_name = os.path.join(directory_name, 'sample_example.txt')
print('Creating', file_name)
with open(file_name, 'wt') as f:
	f.write('sample example file')
print('Cleaning up')
os.unlink(file_name)
os.rmdir(directory_name)	# Will delete the directory

