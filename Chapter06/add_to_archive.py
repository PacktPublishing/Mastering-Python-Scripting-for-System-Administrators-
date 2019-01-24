import shutil
import os
import tarfile

print('creating archive')
shutil.make_archive('work', 'tar', root_dir='..', base_dir='work',)

print('\nArchive contents:')
with tarfile.open('work.tar', 'r') as t_file:
	for names in t_file.getnames():
		print(names)

os.system('touch sample.txt')
print('adding sample.txt')
with tarfile.open('work.tar', mode='a') as t:
	t.add('sample.txt')

print('contents:',)
with tarfile.open('work.tar', mode='r') as t:
	print([m.name for m in t.getmembers()])
