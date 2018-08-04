'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
NU_M = int(input())
C_O = 1
while C_O <= NU_M:
    if C_O%3 == 0 and C_O%5 == 0:
        print("fizz")
        print("Buzz")
    elif C_O%3 == 0:
        print("Fizz")
    elif C_O%5 == 0:
        print("Buzz")
    else:
        print(C_O)
    C_O = C_O + 1
