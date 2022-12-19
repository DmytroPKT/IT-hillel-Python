"""1. Написать калькулятор для простых операций(+,-,*,/,**),
Операнды и оператор вводятся с клавиатуры отдельно(отдельные переменные)"""

s
first_digit = float(input("""Welcome to calculator. 
Choose first digit, onward  press:
'+' for Addition; 
'-' for Subtraction;
'*' for Multiplication; 
'/' for Division;
'**' for Exponentiation.\n
Enter first digit: """))                           # Description of calculator operations and entering the first number.
user_choice = input("Select operation: ")          # User selects an operation
second_digit = float(input("Enter second digit: "))  # User selects second digit
result = 0                                         # The result is 0 at the beginning

if user_choice == "/" and second_digit == 0:       # Checking for division by zero
    print("Can't divide by 0, please restart calculator.")
elif user_choice == "+":                           # Addition
    result = first_digit + second_digit
elif user_choice == "-":                           # Subtraction
    result = first_digit - second_digit
elif user_choice == "*":                           # Multiplication
    result = first_digit * second_digit
elif user_choice == "/":                           # Division
    result = first_digit / second_digit
elif user_choice == "**":                          # Exponentiation
    result = first_digit ** second_digit
else:
    print('Incorrect operation, please restart calculator.')    # Checking for the correctness of the entered operation
    exit()
print(f'Result = {result}')                        # Result
