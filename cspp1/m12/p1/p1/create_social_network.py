'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    adict = {}
    new_list = list(data)
    count_1 = 0
    #count_2 = 0
    check_x = ''
    check_y = ''
    check_e = 0
    check_z = 0
    for char in new_list:
        check_x = check_x + char
        count_1 = count_1 + 1
        if char == ' ':
            print(char)
            print(count_1)
            check_z = check_x
            for _ in range(count_1, len(new_list), 1):
                check_y = check_y + char
                print(check_y)
                check_e = check_e + 1
            print(check_e)
            print(check_y)
            # adict[1]=s
    adict[check_z] = check_y
    print(adict)
        # if char=='\n':
        #     h=c+e
        #     print(h)
        #     for i in range(c+e,len(data),1):
        #         d=d+char
        #         print(d)
    # print(s)
    # print(d)
    # return d





def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
