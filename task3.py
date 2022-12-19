"""3. Определить является ли введенное с клавиатуры число простым
(делится без остатка только на себя и единицу)"""

s
input_number = int(input('Enter number: '))             # Entering a number
if input_number == 2:                                   # Input number is 2
    print('2 is a prime number')
    exit()
for i in range(2, input_number):                        # Loop with a range of numbers
    if input_number % i == 0:                           # Number is divisible by other numbers
        print(f'{input_number} is not a prime number')
        exit()
print(f'{input_number} is a prime number')
