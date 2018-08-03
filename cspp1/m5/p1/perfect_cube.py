"""
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
"""
def main():
    """
    program to check the cube root using guess and check.
    """
    inp_a = int(input())
    guess_i = 0
    while guess_i**3 < inp_a:
        guess_i += 1
    if guess_i**3 == inp_a:
        print(str(inp_a)+ " is a perfect cube")
    else:
        print(str(inp_a" is not a perfect cube")
if __name__ == "__main__":
    main()
    