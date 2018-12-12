import pyAesCrypt
from os import stat, remove

bufferSize = 64 * 1024
password = "#Training"

encFileSize = stat("sample.txt.aes").st_size

with open("sample.txt.aes", "rb") as fIn:
	with open("sampleout.txt", "wb") as fOut:
		try:
			pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
		except ValueError:
			remove("sampleout.txt")
