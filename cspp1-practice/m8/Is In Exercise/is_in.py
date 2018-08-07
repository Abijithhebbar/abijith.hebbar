"""# Exercise: Is In
# Write a Python function, isIn(char, aStr),
 that takes in two arguments a character and String and
  returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character
 and String and returns one boolean value.
"""
def is_in(char_in, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    for i in range(len(a_str)+1):
        if char_in in a_str:
            return True

        return False
def main():
    """ main """
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))
if __name__ == "__main__":
    main()
