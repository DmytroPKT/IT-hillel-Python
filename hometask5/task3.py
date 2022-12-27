"""
3) У вас есть список my_list с значениями типа int.
Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
Количество элементов в списке можно получить с помощью функции len(my_list)
"""


from random import randint
my_list = [randint(1, 50) for i in range(randint(1, 4))]       # random range list
print(my_list)
if len(my_list) < 2:            # Add '0' in case if list elements < 2
    my_list.append(0)
elif len(my_list) >= 2:         # The sum of the last two elements will be added to the list if list's elements > 2
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)
