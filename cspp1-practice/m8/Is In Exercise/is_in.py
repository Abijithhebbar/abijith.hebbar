# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    b=0
    c=0
    for i in range(len(a_str)+1):
        if char in a_str:
            b += 1
    if b >=1:
        return True
    else:
        return False

def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
    main()