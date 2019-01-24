import tarfile
import shutil
import sys

shutil.make_archive(
	'work', 'gztar',
	root_dir='..',
	base_dir='work',
)

print('\nArchive contents:')
with tarfile.open('work.tar.gz', 'r') as t_file:
	for names in t_file.getnames():
		print(names)
