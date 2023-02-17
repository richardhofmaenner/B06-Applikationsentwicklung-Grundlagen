# Integer
my_int = 42
# Output: my_int is of type <class 'int'> and value is 42
print(f"my_int is of type {type(my_int)} and value is {my_int}")

# float
my_float = 23.5
# Output: my_float is of type <class 'float'> and value is 23.5
print(f"my_float is of type {type(my_float)} and value is {my_float}")

# boolean
my_bool = True  # or False
# Output: my_float is of type <class 'bool'> and value is True
print(f"my_float is of type {type(my_bool)} and value is {my_bool}")

# strings
my_str = "hello world"
# Output: my_str is of type <class 'str'> and value is 'hello world'
print(f"my_str is of type {type(my_str)} and value is '{my_str}'")

# list
my_list = [my_int, my_float, my_bool, my_str, None]
# Output: my_list is of type <class 'list'> and value is [42, 23.5, True, 'hello world', None]
print(f"my_list is of type {type(my_list)} and value is {my_list}")

# dictionary
my_dict = {'my_int': my_int, 'my_float': my_float, 'my_str': my_str}
# Output: my_dict is of type <class 'dict'> and value is {'my_int': 42, 'my_float': 23.5, 'my_str': 'hello world'}
print(f"my_dict is of type {type(my_dict)} and value is {my_dict}")

# tuple
my_tuple = (my_int, my_float, my_bool, my_str, None)
# Output: my_tuple is of type <class 'tuple'> and value is (42, 23.5, True, 'hello world', None)
print(f"my_tuple is of type {type(my_tuple)} and value is {my_tuple}")
