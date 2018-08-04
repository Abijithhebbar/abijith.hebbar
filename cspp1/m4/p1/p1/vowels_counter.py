    """"#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
 if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
"""
def main():
    """
    main function
    """ 
    var_a = input()
    v_str = ""
    c_str = ""
    for char in var_a:
        if char in 'AEIOUaeiou':
            v_str += char
        else:
            c_str += char
    print(len(v_str))
if __name__ == "__main__":
    main()
