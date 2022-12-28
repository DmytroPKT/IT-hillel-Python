"""
*4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
Если my_list [1,2,3,4], то new_list [2,3,4,1]
"""
from random import randint

my_list = [randint(1, 50) for i in range(randint(3, 7))]  # Random numbers list with range (3-7)
print('my_list:', my_list)
new_list = my_list[1::]     # my_list elements from index "1" added to new_list
new_list.append(my_list[0])     # my_list element with index "0" added at the end of new_list
print('new_list:', new_list)

