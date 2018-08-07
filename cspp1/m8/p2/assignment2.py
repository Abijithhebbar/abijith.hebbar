"""# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one.
# This function takes in one number and returns one number.
"""
def sumof_digits(input_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if input_n == 0:
        return 0
    return (input_n % 10) + sumof_digits(input_n//10)
def main():
    '''main'''
    inp_a = input()
    print(sumof_digits(int(inp_a)))
if __name__ == "__main__":
    main()
