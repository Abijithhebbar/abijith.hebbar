""" Write a python program to find the square root of the given number
using approximation method
"""

def main():
    """ square root program approximation method"""
    inp_a = int(input())
    guess_a = 0
    check_a = 0.01
    # check is just a tollerance value to check
    while abs(guess_a**2 - inp_a) >= check_a and guess_a <= inp_a:
        guess_a += 0.1
    if abs(guess_a**2 - inp_a) >= check_a:
        print(str(guess_a))
    else:
        print(str(guess_a))
if __name__ == "__main__":
    main()
