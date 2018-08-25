'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(inp_string):
	new_string = ""
	for word in inp_string:
		if word not in "`~!@#$%^&*()_+=- \''":
			new_string += word
	return new_string

def main():
    inp_string = input()
    print(clean_string(inp_string))

if __name__ == '__main__':
    main()
