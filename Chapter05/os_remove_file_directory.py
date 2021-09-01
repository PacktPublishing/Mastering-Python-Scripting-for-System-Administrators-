import os

filen=input("enter file name to remove")
os.remove(str(filen))
print("File removed successfully")

dirn=input("enter directory name to remove")
os.rmdir(str(dirn))
print("Directory removed successfully")
