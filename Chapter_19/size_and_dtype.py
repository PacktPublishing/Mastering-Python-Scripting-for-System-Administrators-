import numpy as np

my_list1 = [1,2,3,4]
my_list2 = [11,22,33,44]

my_lists = [my_list1,my_list2]

my_array = np.array(my_lists)

print(my_array)

size = my_array.shape
print(size)

data_type = my_array.dtype
print(data_type)

