"""
*6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
(используйте split и проверку isdigit)
"""

my_str = input("Enter your text: ")
digits_amount = 0

for i in my_str.split():    # Split string cycle
    if i.isdigit():         # Checking if element is digit
        digits_amount += int(i)  # Sum of numeric string values
print(digits_amount)
