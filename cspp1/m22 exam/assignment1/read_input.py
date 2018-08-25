'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    number_of_lines = int(input())
    string_input = ""
    for i in range(number_of_lines):
    	string_input += input() + "\n"
    print(string_input)


if __name__ == '__main__':
    main()
