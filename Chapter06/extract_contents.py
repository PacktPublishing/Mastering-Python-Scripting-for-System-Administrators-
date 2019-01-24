import tarfile
import os

os.mkdir('work')
with tarfile.open('work.tar', 'r') as t:
	t.extractall('work')
print(os.listdir('work'))
