""" # given input product the individual number example 123 output should be  6"""
I_NT = int(input())
I_C = 1
C_O = 1
N_um =1
if I_NT < 0:
    N_UM = -1
else:
    N_UM = 1
while I_NT >= 1:
    C_O = I_NT % 10
    I_C = I_C * C_O
    I_NT = I_NT // 10
print(N_UM*I_C)
