import tarfile

tar_file = tarfile.open("work.tar.gz", "w:gz")
for name in ["welcome.py", "hello.py", "hello.txt", "sample.txt", "sample1.txt"]:
	tar_file.add(name)
tar_file.close()
