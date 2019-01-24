import re
from collections import Counter

r_e = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1}'

with open("access.log") as f:
	print("Reading Apache log file")
	Apache_log = f.read()
	get_ip = re.findall(r_e,Apache_log)
	no_of_ip = Counter(get_ip)
	for k, v in no_of_ip.items():
		print("Available IP Address in log file " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))

