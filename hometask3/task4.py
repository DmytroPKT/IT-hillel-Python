"""*(НЕОБЯЗАТЕЛНО! НА ОЦЕНКУ НЕ ВЛИЯЕТ)
Создайте приложение подбирающее правильное окончание к фразе:
 "Маша нашла в лесу {К} гриб...". K пользователь вводит с клавиатуры.
Например: Маша нашла в лесу 7 грибОВ.
Маша нашла в лесу 32 грибА."""
s
mushrooms = int(input('Enter the number of mushrooms: '))           # Input quantity of mushrooms.
ending = ''                                                         # End of sentence. Empty by default.
if mushrooms % 10 == 1 and mushrooms % 100 != 11:                   # Ending for 1,21,31.. etc.
    ending = '.'
elif 2 <= mushrooms % 10 <= 4 and not 12 <= mushrooms % 100 <= 14:  # Ending for 2,3,4,22,23,24.. etc.
    ending = 'a.'
else:                                                               # Other endings
    ending = 'ов.'
print(f"Маша нашла в лесу {mushrooms} гриб{ending}")                # Result
