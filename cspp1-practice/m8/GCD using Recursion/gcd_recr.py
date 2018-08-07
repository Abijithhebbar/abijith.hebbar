"""# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b),
 that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
"""
def gcd_recur(int_a, int_b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    """
    if int_b == 0:
        return int_a
    else:
        return gcd_recur(int_b, int_a % int_b)
def main():
    """ main """
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
