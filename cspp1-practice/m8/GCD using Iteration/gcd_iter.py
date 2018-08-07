"""# Exercise: GCDIter
# Write a Python function, gcdIter(a, b),
 that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number."""
def gcd_iter(inp_x, inp_y):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    """
    if inp_x > inp_y:
        smaller = inp_y
    else:
        smaller = inp_x
    for i in range(1, smaller+1):
        if((inp_x % i == 0) and (inp_y % i == 0)):
            hcf = i
    return hcf
def main():
    """ main
    """
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
