import os

inp=input("enter f for deleting a file, d for a directory")
if inp == "f":
    os.remove('sample.txt')
    print("File removed successfully")
elif inp == "d":
    os.rmdir('work1')
    print("Directory removed successfully")
else:
    print("wrong input")
