""""Write a python program to find the square root of the given number
using approximation method
"""
def main():
    """bisection method"""
    inp_a = int(input())
    check_i = 0.01
    low_c = 0
    high_c = inp_a
    guess_i = (high_c + low_c)/2.0
    while abs(guess_i**2 - inp_a) >= check_i:
        if guess_i**2 < inp_a:
            low_c = guess_i
        else:
            high_c = guess_i
        guess_i = (high_c + low_c)/2.0
    print(guess_i)
if __name__ == "__main__":
    main()
