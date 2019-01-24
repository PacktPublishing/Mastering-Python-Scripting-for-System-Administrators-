import telnetlib
import getpass
import sys

HOST_IP = "your host ip address"
host_user = input("Enter your telnet username: ")
password = getpass.getpass()

t = telnetlib.Telnet(HOST_IP)
t.read_until(b"Username:")
t.write(host_user.encode("ascii") + b"\n")
if password:
	t.read_until(b"Password:")
	t.write(password.encode("ascii") + b"\n")

t.write(b"enable\n")
t.write(b"enter_remote_device_password\n") #password of your remote device
t.write(b"conf t\n")
t.write(b"int loop 1\n")
t.write(b"ip add 10.1.1.1 255.255.255.255\n")
t.write(b"int loop 2\n")
t.write(b"ip add 20.2.2.2 255.255.255.255\n")
t.write(b"end\n")
t.write(b"exit\n")
print(t.read_all().decode("ascii") )

