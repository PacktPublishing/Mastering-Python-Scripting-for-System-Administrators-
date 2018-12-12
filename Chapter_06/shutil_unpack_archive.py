import pathlib
import shutil
import sys
import tempfile

with tempfile.TemporaryDirectory() as d:
	shutil.unpack_archive('work.tar.gz', extract_dir='/home/student/work',)
	prefix_len = len(d) + 1
	for extracted in pathlib.Path(d).rglob('*'):
		print(str(extracted)[prefix_len:])
