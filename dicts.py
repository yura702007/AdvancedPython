my_dict = {'name': 'Max', 'age': 42, 'city': 'Boston'}
my_dict_2 = {'name': 'Max', 'age': 42, 'e-mail': 'max@mail.com'}
my_dict.update(my_dict_2)
print(my_dict)
my_dict = {x: x * x for x in range(11)}
print(my_dict)
print(list(my_dict.values()))
