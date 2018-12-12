import tarfile

tar_file = tarfile.open("work.tar.gz", "r:gz")
print(tar_file.getnames())

