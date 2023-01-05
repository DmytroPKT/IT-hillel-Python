"""
*4. Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k,
сдвинув влево все элементы, стоящие правее элемента с индексом k.
- Программа получает на вход список (можно сгенерировать при помощи генератора случайных чисел),
затем число k. Программа сдвигает все элементы, а после этого удаляет
последний элемент списка при помощи метода pop() без параметров.
- Программа должна осуществлять сдвиг непосредственно в списке,
а не делать это при выводе элементов. Также нельзя использовать дополнительный список.
Также не следует использовать метод pop(k) с параметром или оператор del.
"""

from random import randint

my_list = [randint(-999, 999) for i in range(0, 15)]  # Random range list
print('my_list(initial): ', my_list)

k = int(input('Enter the index of the number you want to remove: '))  # Input item index
for s in range(k + 1, len(my_list)):    # Cycle for my_list from (input index + 1) to the end
    my_list[s - 1] = my_list[s]         # Changing items in my_list from k to the end
my_list.pop()                           # Cutout of the last item, because last 2 are the same
print('my_list(output): ', my_list)
