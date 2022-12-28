"""
*5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
Пересоздавать список нельзя! (используйте метод pop)
"""

from random import randint

my_list = [randint(0, 50) for i in range(7)]    # Random numbers list with range 7
print(my_list)
my_list.append(my_list.pop(0))  # Index[0] element from my_list removed and shifted to the end
print(my_list)
