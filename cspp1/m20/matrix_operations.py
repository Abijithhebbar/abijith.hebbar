def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # pass
    a = len(matrix_1)
    b = len(matrix_1[0])
    c = len(matrix_2)
    d = len(matrix_2[0])
    h = []
    h = [0]*a
    for i in range(d):
        h[i] = [0]*d
    # print(h)
    if b == c:
        # for i in range(a):
        #     for j in range(b):
        #         # k[i][j]=0
        #         k.append(k[i][j])

        for i in range(a):
            for j in range(d):
                for x in range(c):
                    h[i][j] += matrix_1[i][x]*matrix_2[x][j]
                    # print(k[i][j])
                #+ matrix_1[i][j]*matrix_2[j+1][i] + matrix_1[i][j]*matrix_2[j+2][i])
        return h
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    # pass

    a = len(matrix_1)
    b = len(matrix_1[0])
    c = len(matrix_2)
    d = len(matrix_2[0])
    k = []
    k =[0]*a
    for i in range(b):
        k[i] = [0]*b
    print(k)
    # h = []
    # q = []
    # g = []
    # # 
    # if a == c and b == d:
    #     for i in range(a):
    #         for j in range(b):
    #             k[i][j] = matrix_1[i][j]+matrix_2[i][j]
    #     # k += i+j
    #     # x = len(k)
    #     # z=x//2
    #     # z=z+1
    #     # for y in range(x):
    #     #     if y<=(x/2)-1:
    #     #         # print(z)
    #     #         h.append(k[y])
                
                
                
        #     elif y>=(x/2):
        #         q.append(k[y])
        # l = len(h)
        # for i in range(l):
           
        #     g.append(h[i]+q[i])
        # print(g)
                

        #for x in k:
        return k

            

    else:
        print("Error: Matrix shapes invalid for addition")
        return None
   


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    pass

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    #pass
    n = []
    for i in range(1):
        n += input().split(',')
    #print(n)
    a = int(n[0])
    b = int(n[1])
    matrix_1 = []
    for i in range(a):
        matrix_1.append(list(map(int, input().rstrip().split())))
    #print(matrix_1)
    m = []
    for i in range(1):
        m += input().split(',')
    #print(m)
    matrix_2 = []
    c = int(m[0])
    d = int(m[1])
    for i in range(c):
        matrix_2.append(list(map(int, input().rstrip().split())))
    #print(matrix_2)
    # print(mult_matrix(matrix_1, matrix_2))
    print(add_matrix(matrix_1, matrix_2))
    print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
