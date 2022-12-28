"""
3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на четных местах из
my_list_1, а потом все элементы на нечетных местах из my_list_2.
"""

from random import randint
my_list_1 = [randint(1, 900) for i in range(7)]     # First random number list with range 7
print(my_list_1)
my_list_2 = [randint(1, 900) for s in range(7)]     # Second random number list with range 7
print(my_list_2)
my_result = []
for d in range(len(my_list_1)):     # Even / odd index cycle
    my_result.append(my_list_1[d])  # Append my_list1 integers to my_result even indices
    for f in range(d, d+1):
        my_result.append((my_list_2[f]))  # Append my_list2 integers to my_result odd indices
print(my_result)
