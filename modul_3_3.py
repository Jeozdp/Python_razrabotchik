def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()

list_ = [1,2,3]

print_params (b= 25)
print_params(c = list_)


values_list = ['Привет', 999, [6, 2, 9]]
values_dict = {'a': [1, 7, 11], 'b': 'Пока', 'c': 998}

print_params(*values_list)

print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)