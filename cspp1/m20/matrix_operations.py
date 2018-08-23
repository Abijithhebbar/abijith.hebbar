def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows_matrix_1 = len(matrix_1)
    columns_matrix_1 = len(matrix_1[0])
    rows_matrix_2 = len(matrix_2)
    columns_matrix_2 = len(matrix_2[0])
    result_mul = [[0 for j in range(len(matrix_1))]for i in range(len(matrix_1[0]))]
    if columns_matrix_1 == rows_matrix_2:
        for i in range(rows_matrix_1):
            for j in range(columns_matrix_2):
                for k in range(rows_matrix_2):
                    result_mul[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return result_mul
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
    rows_matrix_1 = len(matrix_1)
    columns_matrix_1 = len(matrix_1[0])
    rows_matrix_2 = len(matrix_2)
    columns_matrix_2 = len(matrix_2[0])
    result_add = [[0 for j in range(len(matrix_1))]for i in range(len(matrix_1[0]))]
    if rows_matrix_1 == rows_matrix_2 and columns_matrix_1 == columns_matrix_2:
        for i in range(rows_matrix_1):
            for j in range(columns_matrix_2):
                result_add[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return result_add
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
    rows_columns = []
    for i in range(1):
        rows_columns += input().split(',')
    matrix_ = []
    rows_ = int(rows_columns[0])
    columns_ = int(rows_columns[1])
    for i in range(rows_):
        matrix_.append(list(map(int, input().rstrip().split())))
    # print(len(matrix_))
    # print(len(matrix_[0]))
    # print(rows_columns[1])
    # print(rows_columns[0])
    if len(matrix_) == rows_columns[0] and len(matrix_[0]) == rows_columns[1]:
        print("Error: Invalid input for the matrix")
        return None
    else:
        return matrix_
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    matrix_1= read_matrix()
    matrix_2 = read_matrix()
    print(add_matrix(matrix_1, matrix_2))
    print(mult_matrix(matrix_1, matrix_2))


if __name__ == '__main__':
    main()
