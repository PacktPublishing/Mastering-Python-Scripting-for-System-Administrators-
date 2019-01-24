import json

python_dict =  {"Name": "Harry", "Age": 26}
python_list =  ["Mumbai", "Pune"]
python_tuple =  ("Basketball", "Cricket")
python_str =  ("hello_world")
python_int =  (150)
python_float =  (59.66)
python_T =  (True)
python_F =  (False)
python_N =  (None)

json_obj = json.dumps(python_dict)
json_arr1 = json.dumps(python_list)
json_arr2 = json.dumps(python_tuple)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
json_n = json.dumps(python_N)

print("json object : ", json_obj)
print("jason array1 : ", json_arr1)
print("json array2 : ", json_arr2)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
print("json true", json_t)
print("json false", json_f)
print("json null", json_n)

