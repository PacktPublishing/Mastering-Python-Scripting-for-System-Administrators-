import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "#Training"

# encrypt
with open("sample.txt", "rb") as fIn:
	with open("sample.txt.aes", "wb") as fOut:
		pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size
encFileSize = stat("sample.txt.aes").st_size
