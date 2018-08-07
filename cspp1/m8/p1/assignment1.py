"""# Exercise: Assignment-1
# Write a Python function, factorial(n),
 that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number.
"""
def fact_out(n_fact):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n_fact == 0:
        return 1

    return n_fact * fact_out(n_fact-1)
def main():
    """ main """
    input_a = input()
    print(fact_out(int(input_a)))

if __name__ == "__main__":
    main()
