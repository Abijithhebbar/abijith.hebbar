'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
    """defining main Subset """
    inp_vara = input()
    #input string S
    inp_varb = 'bob'
    count_o = 0
    for i in range(len(inp_vara)):
        if inp_varb == inp_vara[i:i+3]:
            count_o = count_o + 1
    print(str(count_o))
if __name__ == "__main__":
    main()
