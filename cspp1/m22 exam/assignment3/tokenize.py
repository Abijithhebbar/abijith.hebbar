'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
# output_dictionary = {}
def tokenize(string_input):
    """Tokenize function"""
    output_dictionary = {}
    for word in string_input:
        if word not in "`~!@#$%^&*()_+=.-\''":
            new_string += word
    list_input = new_string.split()
    for word in list_input:
        if word in output_dictionary:
            output_dictionary[word] += 1
        else:
            output_dictionary.update({word:1})
    return output_dictionary
    # for key in list_input:
    #     key = re.sub('[^a-zA-z0-9]', '', key)
    #     if key not in output_dictionary:
    #         output_dictionary[key] = 1
    #     else:
    #         output_dictionary[key] += 1
def main():
    """main function"""
    number_of_lines = int(input())
    string_input = ""
    for _ in range(0, number_of_lines, 1):
        string_input += input()
        tokenize(string_input)
    print(tokenize(string_input))

if __name__ == '__main__':
    main()
