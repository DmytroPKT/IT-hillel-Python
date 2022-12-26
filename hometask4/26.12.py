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
my_set = set([1, 2, 3, 4, 5, 6])
print(my_set)
my_set.add(33)
print(my_set)
my_set = {'q', 'w', 'e', 'r', 't', 'Z'}
print(my_set)
my_set.add(33)
print(my_set)

# my_string = "11 footbolistov za 5 let zabili 231 gol v 102 matchah"
# my_set = set(my_string)
# print(my_set)

# my_set.update('Odarka!@#$%^&*()_+')
# print(my_set)

# udalenie
my_set.discard('r')
print(my_set)

my_set.discard('Z') # discard - iskluchaet element, v sluchae ego otsutstviya vo mnozhestve net oshibki
print(my_set)

my_set.remove(33)
print(my_set)




