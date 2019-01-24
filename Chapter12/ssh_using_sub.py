import subprocess
import sys

HOST="your host username@host ip"
COMMAND= "ls"

ssh_obj = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

result = ssh_obj.stdout.readlines()
if result == []:
    err = ssh_obj.stderr.readlines()
    print(sys.stderr, "ERROR: %s" % err)
else:
    print(result)

