'''
    Document Distance - A detailed description is given in the PDF
'''
import math
file_name = "stopwords.txt"
def similarity(dict_1, dict_2):
    '''
        Compute the document distance as given in the PDF
    '''
    list_1 = ""
    list_2 = ""
    for _ in dict_1:
    	if _ not in '!@#$%^&*()_+-=?':
    		list_1 += _
    for _ in dict_2:
    	if _ not in '!@#$%^&*()_+-=?':
    		list_2 += _
    list_1 = list_1.split()
    list_2 = list_2.split()
    list_5 = list_1 +list_2
    adict = {}
    for word in list_5:
    	if word not in load_stopwords(file_name).keys():
    		adict[word] = (list_1.count(word), list_2.count(word))
    numerator, add_1, add_2 = 0, 0, 0
    for a_check in adict:
    	numerator += adict[a_check][0]*adict[a_check][1]
    	add_1 += adict[a_check][0] ** 2
    	add_2 += adict[a_check][1] ** 2
    	denominator = math.sqrt(add1) * math.sqrt(add2)
    value_check = numerator/denominator
    return value_check
   
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input().lower()
    
    input2 = input().lower()
    

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
