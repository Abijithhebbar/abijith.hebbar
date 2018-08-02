"'# In a given string we should find the number of vowels in lower case'"
INP_VAR = input("Enter text")
VOWELS_STR = ""
CONSONENTS_STR = ""
for char in INP_VAR:
    if char in 'aeiou':
        VOWELS_STR += char
    else:
        CONSONENTS_STR += char
print("no of vowels are", len(VOWELS_STR))
