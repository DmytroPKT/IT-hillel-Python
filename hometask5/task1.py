"""
1) У вас есть список my_list с значениями типа int.
Распечатать те значения, которые больше 100.
Задание выполнить с помощью цикла for.
"""
from random import randint
my_list = [randint(1, 999) for i in range(randint(1, 40))]      # random range list
print(my_list)
for element in my_list:          # cycle for elements > 100
    if element > 100:
        print(element, end=" ")  # print elements > 100
