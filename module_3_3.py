def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params()
print_params(a=9, b="Bla-bla", c=False)
print_params(a=1)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [1, "str", True]
values_dict = {"a": 1, "b": "строка", "c": True}


print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Cтрока"]
print_params(*values_list_2, 42)