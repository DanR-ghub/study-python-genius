#------------
string_var = "Hello, Python!"
integer_var = 42
float_var = 3.14
bool_var = True
list_var = [1, 2, 3]
dict_var = {"name": "name1", "second_name": "name2"}
tuple_var = (1, 2, 3)
none_var = None
#------------
print(integer_var > 10)
print(float_var == 3.14)

print(string_var == "Hello, Python!")
print("a" > "b")

print(bool_var and False)
print(not bool_var)

print(list_var == [1, 2, 3])
print(list_var < [1, 2, 4])

print(dict_var == {"key1": "value1", "key2": "value2"})

print(tuple_var > (1, 2, 2))
#------------
num_str = 125
num_str = str(num_str)

message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print(message)

split_test = 'This is a split test'
split_list = split_test.split()
string_join = ' '.join(split_list)
length = len(string_join)
#------------
list_append = [1, 2, 3]
list_append.append(4)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
index = list_extend.index(6)
length_list = len(list_append)
#------------
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

keys = dict_test.keys()
values = dict_test.values()
print(keys)
print(values)

items = dict_test.items()
print(items)
#------------
