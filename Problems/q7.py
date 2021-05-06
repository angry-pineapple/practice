#Rotate a matrix clock-wise and anti-clockwise
"""
Rotating a matrix clockwise or anticlockwise-

Normal..........clockwise............. Anti-clockwise
1 2 3.          7 4 1.                  3 6 9
4 5 6.       => 8 5 2.                =>2 5 8
7 8 9.          9 6 3.                  1 4 7

Clockwise - transpose, then reverse horizontally
Anti-clockwise- reverse horizontally, then transpose

STEPS=
Transpose
1 4 7
2 5 8
3 6 9
Then,
Reverse(horizontally, for clockwise)
7 4 1
8 5 2
9 6 3
_____
Or, reverse (horizontally, for anti clockwise)
3 2 1
6 5 4
9 8 7
Then
Transpose
3 6 9
2 5 8
1 4 7
"""

def reverse_by_rows(matrix):
    row_reversed_matrix = []
    for rows in matrix:
        new_row = rows[::-1]
        row_reversed_matrix.append(new_row)
    return row_reversed_matrix

def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    #Temp matrix filled with zeros. Fill values from matrix's row to temp matrix's colum
    result = []
    for i in range(row):
        result.append([0]*col)
    for i in range(row):
        for j in range(col):
            result[i][j] = matrix[j][i]
    return result

def get_anti_clockwise(matrix):
    #Reverse rows horizontally
    row_reversed_matrix = reverse_by_rows(matrix)
    #Transpose
    transposed_matrix = transpose(row_reversed_matrix)
    return transposed_matrix

def get_clockwise(matrix):
    #Transpose
    transposed_matrix = transpose(matrix)
    #Reverse rows Horizontally
    row_reversed_matrix = reverse_by_rows(transposed_matrix)
    return row_reversed_matrix

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end=" ")
        print("")

if __name__ == "__main__":
    matrix =[
            ['*','*','*','*'],
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
            ]
    # Note that num of row == num of col for this algorithm
    print("Original matrix -")
    print_matrix(matrix)
    clockwise_matrix = get_clockwise(matrix)
    print("\nClockwise-")
    print_matrix(clockwise_matrix)
    anti_clockwise_matrix = get_anti_clockwise(matrix)
    print("\nAnti-Clockwise-")
    print_matrix(anti_clockwise_matrix)
