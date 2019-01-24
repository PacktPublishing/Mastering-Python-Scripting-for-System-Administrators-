import resource
import sys
import signal
import time
def time_expired(n, stack):
	print('EXPIRED :', time.ctime())
	raise SystemExit('(time ran out)')
signal.signal(signal.SIGXCPU, time_expired)
# Adjust the CPU time limit
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Soft limit starts as  :', soft)
resource.setrlimit(resource.RLIMIT_CPU, (10, hard))
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Soft limit changed to :', soft)
print()
# Consume some CPU time in a pointless exercise
print('Starting:', time.ctime())
for i in range(200000):
	for i in range(200000):
		v = i * i
# We should never make it this far
print('Exiting :', time.ctime())

