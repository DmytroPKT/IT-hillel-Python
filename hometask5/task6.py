"""
*6. Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
 Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
- Примечание. Эту задачу можно решить в одну строчку.
"""

# First option
from random import randint  # random range list

my_list1 = [randint(1, 100) for i in range(4)]
my_list2 = [randint(1, 100) for s in range(4)]
my_list_general = set(my_list1 + my_list2)  # Separating duplicate numbers with 'set'

print('my_list01:', my_list1)
print('my_list02:', my_list2)
print('my_list_general:', my_list_general)
print('Number of unique numbers:', len(my_list_general), '\n')

# Second option

# random range list with set of two lists
second_option = set([randint(1, 10) for d in range(randint(1, 10))] + [randint(1, 10) for f in range(randint(1, 10))])
print('Second option.\n', second_option)
print('Number of unique numbers:', len(second_option))
