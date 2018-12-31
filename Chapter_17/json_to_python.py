import json

j_obj =  '{ "Name":"Harry", "Age":26, "Department":"HR"}'

p_obj = json.loads(j_obj)

print(p_obj)
print(p_obj["Name"])
print(p_obj["Department"])

