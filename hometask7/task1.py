"""
1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
    а) Создать список и поместить туда имя самого молодого человека.
        Если возраст совпадает - поместить все имена самых молодых.
    б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
    в) Посчитать среднее количество лет всех людей из начального списка.
"""

persons = [
    {'name': 'Foltest', 'age': '44'},
    {'name': 'Radovid', 'age': '34'},
    {'name': 'Emgyr', 'age': '56'},
    {'name': 'Sigismund', 'age': '41'},
    {'name': 'Sigismund', 'age': '34'}
]

"""
а) Создать список и поместить туда имя самого молодого человека.
        Если возраст совпадает - поместить все имена самых молодых.
"""
ages_list = []  # Ages list (empty by default)
youngest_list = []  # The youngest persons list (empty by default)

for i in persons:   # Cycle for dictionary list
    ages_list.append(i['age'])  # Addition to the "ages_list" ages of persons
ages_list.sort()    # Ages list sorting
for s in persons:   # Second cycle for dictionary list
    if ages_list[0] == s['age']:  # Condition for cycle elements
        youngest_list.append(s['name'])  # Addition to the "youngest_list" name(s) of the youngest persons
print('The youngest person(s):', youngest_list)


"""
б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
"""
names_length = []  # Names length list (empty by default)
longest_names = []  # Longest names list (empty by default)

for d in persons:   # Cycle for dictionary list
    names_length.append(len(d['name']))   # Addition to names_list names length
names_length.sort()   # Names length list sorting
for f in persons:   # Cycle for dictionary list
    if names_length[-1] == len(f['name']):  # Condition for cycle elements
        longest_names.append(f['name'])     # Addition to the 'longest_names' persons with the longest names
print('The longest name(s) person(s): ', longest_names)


"""
в) Посчитать среднее количество лет всех людей из начального списка.
"""

ages_list2 = [int(a) for a in ages_list]  # Second ages list with elements as integers
# Average age calculation as summary of all ages divided by persons quantity
print('Average age: ', (sum(ages_list2))/len(persons))
