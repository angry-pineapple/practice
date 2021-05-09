# Set Matrix Zeros
"""
idea:
take 2 arrays - row_zero & col_zero
Traverse row-wise, if row contains zero, add "T" to row_zero, else add "F".
Traverse column-wise, if column contains zero, add "T" to col_zero, else add "F".

Traverse the matrix=>
for all (row-index,col-index):
    if corresponding (row-index) in row_zero is "T" or if corresponding (col-index) in col_zero is "T":
        matrix[row-index][col-index]=0 (set current element zero)
    else:
        leave it as it is.


TODO
 Don't use extra space for row_zero & col_zero.
 Use first row and first col as the row_zero & col_zero arrays,
 and perform the same method on the matrix of size (row-1)*(col-1)

"""


def set_zero_matrix(matrix):
    col_zero = []
    row_zero = []
    for row in matrix:
        if 0 in row:
            row_zero.append("T")
        else:
            row_zero.append("F")

    for i in range(0, len(matrix[0])):
        col_list = []
        for j in range(0, len(matrix)):
            col = matrix[j][i]
            col_list.append(col)
        if 0 in col_list:
            col_zero.append("T")
        else:
            col_zero.append("F")

    print(f"row zero array- {row_zero}, col zero array- {col_zero}")
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if row_zero[i] == "F" and col_zero[j] == "F":
                continue
            else:
                matrix[i][j] = 0

    return matrix

if __name__ == "__main__":
    my_matrix= [[1, 2, 0, 1],
                [3, 0, 9, 9],
                [4, 3, 8, 2],
                [1, 5, 4, 5]
                ]
    print("My original Matrix:-")
    for row in my_matrix:
        print(row)
    print("Setting zeros ...")
    zero_matrix = set_zero_matrix(my_matrix)
    print("My zero Matrix:-")
    for row in zero_matrix:
        print(row)
