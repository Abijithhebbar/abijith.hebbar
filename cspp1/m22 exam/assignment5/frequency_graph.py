'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	"""frequency function"""
	sorted_dict = sorted(dictionary.keys())
	for i in sorted_dict:
		if dictionary[i] == 1:
			j="#"
		if dictionary[i] == 2:
			j="##"
		if dictionary[i] == 3:
			j="###"
		if dictionary[i] == 4:
			j="####"
		if dictionary[i] == 5:
			j="#####"
		if dictionary[i] == 6:
			j="######"
		if dictionary[i] == 7:
			j="#######"
		if dictionary[i] == 8:
			j="########"
		if dictionary[i] == 9:
			j="#########"
		if dictionary[i] == 10:
			j="##########"
		if dictionary[i] == 11:
			j="###########"
		if dictionary[i] == 12:
			j="############"
		if dictionary[i] == 13:
			j="#############"
		if dictionary[i] == 14:
			j="##############"
		if dictionary[i] == 12:
			j="###############"
		print(i, '-', j)

def main():
	"""main function"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
