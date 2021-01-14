person_count = int(input("Please enter the number of people: "))
cake_count = int(input("Please enter the number of cake: "))
matrix = []
for i in range(0, person_count):
    sub_matrix = []
    str_row = input('Please enter row %d: ' % i)
    str_row_item = str_row.split(' ')
    for item in str_row_item:
        sub_matrix.append(float(item))
    matrix.append(sub_matrix)
print('Your input: ')
print(matrix)
col_sum = []
for i in range(0, cake_count):
    col_sum.append(0)
for row in matrix:
    for i, element in enumerate(row):
        col_sum[i] += element

for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        if col_sum[j] == 0:
            matrix[i][j] = -1
        else:
            matrix[i][j] = matrix[i][j] / col_sum[j]

print('plan:')
print(matrix)
