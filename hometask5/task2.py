"""
2) У вас есть список my_list с значениями типа int, и пустой список my_results.
Добавить в my_results те значения, которые больше 100.
Распечатать список my_results.
Задание выполнить с помощью цикла for.
"""

from random import randint
my_list = [randint(1, 999) for i in range(randint(1, 40))]  # random range list
print(my_list)
my_result = []
for element in my_list:     # cycle for list elements > 100
    if element > 100:
        my_result.append(element)   # elements > 100 added to my_result
print(my_result)
