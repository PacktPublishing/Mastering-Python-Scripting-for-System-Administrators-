import tarfile
import time
with tarfile.open('work.tar', 'r') as t:
	for file_info in t.getmembers():
		print(file_info.name)
		print("Size   :", file_info.size, 'bytes')
		print("Type   :", file_info.type)
		print()

