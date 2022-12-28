"""
11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
в строке ТОЛЬКО ОДИН раз.
"""

my_str = tuple('1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, even, odd, creature, python, winston')   # Default string
my_list = []

for i in my_str:    # Cycle for string
    if my_str.count(i) == 1:    # Checking for duplicate elements in a string
        my_list.append(i)       # Adding unique elements to my_list
print(my_list)
