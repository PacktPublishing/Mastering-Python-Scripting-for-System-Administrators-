f=open('/var/log/kern.log','r')
lines = f.readlines()
for line in lines:
	kern_log = line.split()
	print(kern_log)

