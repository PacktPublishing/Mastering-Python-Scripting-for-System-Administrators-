import os

inp=input("enter f for deleting a file, d for a directory")
if inp == "f":
    filen=input("enter file name to remove")
    os.remove(str(filen))
    print("File removed successfully")
elif inp == "d":
    dirn=input("enter directory name to remove")
    os.rmdir(str(dirn))
    print("Directory removed successfully")
else:
    print("wrong input")