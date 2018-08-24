'''Tic_Tac_Toe'''
def tic_tac_toe(matrix):
   '''Tic_Tac_Toe'''
   n = len(matrix[0])
   winner = []
   for row in matrix:
       if len(set(row)) == 1:
           winner.append(row[0])
   for i in range(0, n):
       lis1 = []
       for j in range(0, n):
           lis1.append(matrix[j][i])
       if len(set(lis1)) == 1:
           winner.append(matrix[j][i])
   lis2 = []
   for i in range(0, n):
       lis2.append(matrix[i][i])
   if len(set(lis2)) == 1:
       winner.append(matrix[i][i])
   lis3 = []
   for i in range(0, n):
       lis3.append(matrix[(n-1)-i][i])
   if len(set(lis3)) == 1:
       winner.append(matrix[i][i])
   winner = list(set(winner))
   if winner == []:
       print('draw')
       return None
   if len(winner) == 1:
       if winner[0] == 'x' or winner[0] == 'o':
           print(winner[0])
       else:
           print("invalid input")
       return winner[0]
   else:
       print("invalid game")
       return None
def main():
   '''main'''
   n = int(input())
   matrix = []
   for _ in range(0,n):
       col = input().split(' ')
       matrix.append(col)
   tic_tac_toe(matrix)
if __name__ == '__main__':
   main()