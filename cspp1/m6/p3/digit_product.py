""" # given input product the individual number example 123 output should be  6"""
I_NT = int(input())
I_C = 1
C_O = 1
while I_NT >= 1:
    C_O = I_NT % 10
    I_C = I_C * C_O
    I_NT = I_NT // 10
print(I_C)
