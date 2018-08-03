""" Write a python program to find the square root of the given number
using approximation method
testcase 1
input: 25
output: 4.999999999999998
testcase 2
input: 49
output: 6.999999999999991
"""
def main():
    """ main function """
    inp_var = int(input())
    check_i = 0.01
    guess_i = inp_var/2.0
    while abs(guess_i**2 - inp_var) >= check_i:
        guess_i = guess_i - ((guess_i**2) - inp_var)/(2*guess_i)
    print(guess_i)
if __name__ == "__main__":
    main()
