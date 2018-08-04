'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
S_C = input()
S_CN = ""
for i in S_C:
    if i in '!@#$%^&*()_+-=?':
        S_CN += " "
    else:
        S_CN += i
print(S_CN)
