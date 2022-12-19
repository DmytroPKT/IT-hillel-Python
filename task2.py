"""2. По данному целому числу N распечатайте все квадраты натуральных чисел,
 не превосходящие N, в порядке возрастания.
Например:
50      1 4 9 16 25 36 49
10      1 4 9
100     1 4 9 16 25 36 49 64 81 100"""
s
number = int(input('Enter number: '))          # Entering a number
for i in range(1, number+1):                   # Computation the numbers in square
    if i ** 2 <= number:                       # Requirements for numbers in square
        print(i ** 2, end=" ")                 # Result Output
