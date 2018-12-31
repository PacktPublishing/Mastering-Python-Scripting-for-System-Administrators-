from fabric.api import *

env.hosts=["host_name@host_ip"]
env.password='your password'

def dir():
    run('mkdir fabric')
    print('Directory named fabric has been created on your host network')

def diskspace():
    run('df')

def check():
    host_type()

