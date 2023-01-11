"""
2)Даны два словаря my_dict_1 и my_dict_2.
    а) Создать список из ключей, которые есть в обоих словарях.
    б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
    в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
    г) Объединить эти два словаря в новый словарь по правилу:
        если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
        если ключ есть в двух словарях -
        поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
        {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
"""

my_dict_1 = {10: 10, 20: 10, 30: 15, 45: 15, 50: 86}
my_dict_2 = {10: 20, 20: 22, 45: 32, 75: 99, 100: 1}
print(f'First dictionary: {my_dict_1}', f'Second dictionary: {my_dict_2}', sep="\n")

"""
а) Создать список из ключей, которые есть в обоих словарях.
"""
new_list1 = []  # New list (empty by default)

for i in my_dict_1.keys() & my_dict_2.keys():   # Cycle for keys in two dictionaries
    new_list1.append(i)     # Append keys to new_list1
print("Keys in two dictionaries: ", new_list1)

"""
 б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
"""
# Created list with keys in first dictionary, but not in second
new_list2 = list(my_dict_1.keys() - my_dict_2.keys())
print("Keys in first dictionary, but not in second dictionary: ", new_list2)

"""
 в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
"""

new_dictionary = {}

for s in my_dict_1.keys() - my_dict_2.keys():   # cycle for keys in first dictionary, but not in second dictionary
    new_dictionary[s] = my_dict_1[s]    # add key and value to new_dictionary
print("New dictionary with key/value in first dictionary, but not in second dictionary:", new_dictionary)

"""
г) Объединить эти два словаря в новый словарь по правилу:
        если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
        если ключ есть в двух словарях -
        поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
        {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
"""

new_dictionary2 = {}

for d in my_dict_1.keys() | my_dict_2.keys():  # Cycle for key for both dictionaries

    if d in my_dict_1.keys() & my_dict_2.keys():  # If same keys in both dictionary, combined value
        new_dictionary2[d] = [my_dict_1[d], my_dict_2[d]]

    elif d in my_dict_1.keys() - my_dict_2.keys():  # If keys only in first dictionary, add key and value to new_dict
        new_dictionary2[d] = my_dict_1[d]

    elif d in my_dict_2.keys() - my_dict_1.keys():  # If keys only in second dictionary, add key and value to new_dict
        new_dictionary2[d] = my_dict_2[d]
print("New dictionary combined from both dictionary: ", new_dictionary2)
