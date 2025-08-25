# import re (not used)

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Step 1: Transform the string into a 2D list (matrix)
matrix = [list(row) for row in MATRIX_STR.strip().split('\n')]
print(matrix)


# Step 2: Read column by column, top to bottom, left to right
num_matrix = len(matrix)#find number of rows
num_cols = len(matrix[0])#find number of columns
decoded_chars = []#list to hold decoded characters

for col in range(num_cols):#take each column
    for row in range(num_matrix):#populate list with characters from each row in that column
        if matrix[row][col].isalpha():#check if character is alpha
            decoded_chars.append(matrix[row][col])#append character to list
        else:
            decoded_chars.append(' ')#append space to list

# Join all characters into a string
decoded_str = ''.join(decoded_chars)
# Step 3: Replace multiple spaces with a single space
cleaned_str = ' '.join(decoded_str.split()) #split and join to remove extra spaces
print(cleaned_str)