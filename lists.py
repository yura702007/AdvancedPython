# from copy import copy

list_org = ['banana', 'cherry', 'apple']
new_list = list_org
print(list_org, new_list)
new_list.append('lemon')
print(list_org, new_list)
list_org.pop(2)
print(list_org, new_list)
new_list_2 = new_list.copy()
print(new_list, new_list_2)
new_list_2.append('lime')
print(new_list, new_list_2)
my_list = [i * i for i in range(10) if i % 2 != 0]
print(my_list)
