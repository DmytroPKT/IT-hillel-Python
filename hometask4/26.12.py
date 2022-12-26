# """
# Generator spiskov
# """
#
# from random import randint
# # randint(start, end) - funktciya generiruet slu4ainoe chislo iz diapazona start - end
# print(randint(-22, 9))
# #
# """
# li = [expression i for item in iterable if condition]
# expression - vyrazhenie
# item - element izvlekaemiy iz posledovatelnosti
# iterable - posledovatelnost'
# condition - uslovnaya konstruktsiya, dobavlenie elementa proizoydet tolko esli ona vernet True
# """
# li = [i ** 2 for i in range(10)]
# print(li)
#
# li = [randint(-100, 100) for i in range(20)]
# print(li)
#
# my_string = "11 footbolistov za 5 let zabili 231 gol v 102 matchah"
# li = [word for word in my_string.split() if word.isdigit()]
# print(li)
# li = [word for word in my_string.split() if word.isalpha()]
# print(li)
#
# li = [word for word in my_string if word.isdigit()]
# print(li)
# li = [word for word in my_string if word.isalpha()]
# print(li)

# """
# Kortezh - tip dannyh, yavlyaetsa neizmennym spiskom
# """
#
# tu = tuple([1, 2, 3, 4, 5])
# tu2 = ('1', 2, 3.2, 'Taras')
# tu3 = tuple('apple')
# print(tu)
# print(tu2)
# print(tu3)
# print(tu[2])
# tu4 = (1, 2, 3, ['a', 'b', 'c'])
# tu4[3][1] = 999
# print(tu4)
#
# li = list(tu)
# print(type(li), li)

"""
Mnozhestvo - neuporyadochenniy nabor unikalnyh elementov
"""
# my_set = set([1, 2, 3, 4, 5, 6])
# print(my_set)
# my_set.add(33)
# print(my_set)
# my_set = {'q', 'w', 'e', 'r', 't', 'Z'}
# print(my_set)
# my_set.add(33)
# print(my_set)

# my_string = "11 footbolistov za 5 let zabili 231 gol v 102 matchah"
# my_set = set(my_string)
# print(my_set)

# my_set.update('Odarka!@#$%^&*()_+')
# print(my_set)

# udalenie
# my_set.discard('r')
# print(my_set)
#
# my_set.discard('Z') # discard - iskluchaet element, v sluchae ego otsutstviya vo mnozhestve net oshibki
# print(my_set)
#
# my_set.remove(33)
# print(my_set)

"""
practice
"""

# dano 4islo poschitat kolichestvo nu;ley v nem

# from random import randint
#
# num = randint(99, 99999)
# print(num)
# count_zero = 0
# for symbol in str(num):
#     if symbol == '0':
#         count_zero += 1
# print(count_zero)
# # python stye
# print(str(num).count('0'))

"""
Dano celoe chislo . opredelit kolichestvo nuley v konce chisla. naprimer :
102834000 -  3 nulya
"""

num = 102024000
print(num)
count_zero = 0
while num%10 == 0:
    count_zero += 1
    num //= 10
print(count_zero)

option2 = 102024000
count_zero = 0
for sym in str(num)[::-1]:
    if sym == '0':
        count_zero += 1
    else:
        break
print('option2', count_zero)


option3 = 102024000
count_zero = 0
for index in range(len(str(option3))-1, 0, -1):
    if str(option3)[index] == '0':
        count_zero += 1
    else:
        break
print('option3', count_zero)

option4 = 102024000
print(len(str(option4))) # знал колличество цифр получив строку
print(str(option4)[::-1]) # perevorot chisla prevrashennogo v stroku
print(int(str(option4)[::-1]))  # prevrashenie perevernutoy stroki v chislo
print(len(str(int(str(option4)[::-1]))))  # prevrashenie predidushege deystvie opyat v stroku
count_zero = len(str(option4)) - len(str(int(str(option4)[::-1])))
print('option4', count_zero)
