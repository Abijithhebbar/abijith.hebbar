'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    output = True
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            if j < 8:
                if sudoku[i][j] == sudoku[i][j+1]:
                    output = False
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            if j < 8:
                if sudoku[j][i] == sudoku[j+1][i]:
                    output = False
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if j < 2:
                if sudoku[i][j] == sudoku[i][j+1]:
                    output = False
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if j < 3:
                if sudoku[j][i] == sudoku[j+1][i]:
                    output False
    for i in range(3, 6, 1):
        for j in range(3, 6, 1):
            if j < 5:
                if sudoku[i][j] == sudoku[i][j+1]:
                    output = False
    for i in range(3, 6, 1):
        for j in range(3, 6, 1):
            if j < 5:
                if sudoku[j][i] == sudoku[j+1][i]:
                    output False
    for i in range(6, 9, 1):
        for j in range(6, 9, 1):
            if j < 8:
                if sudoku[i][j] == sudoku[i][j+1]:
                    output = False
    for i in range(6, 9, 1):
        for j in range(6, 9, 1):
            if j < 8:
                if sudoku[j][i] == sudoku[j+1][i]:
                    output False


    return output


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
