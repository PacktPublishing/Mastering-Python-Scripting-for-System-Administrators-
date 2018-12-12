import zipfile
def meta_info(names):
	with zipfile.ZipFile(names) as zf:
		for info in zf.infolist():
			print(info.filename)
			if info.create_system == 0:
				system = 'Windows'
			elif info.create_system == 3:
				system = 'Unix'
			else:
				system = 'UNKNOWN'
			print("System         :", system)
			print("Zip Version    :", info.create_version)
			print("Compressed     :", info.compress_size, 'bytes')
			print("Uncompressed   :", info.file_size, 'bytes')
			print()


if __name__ == '__main__':
	meta_info('work.zip')

