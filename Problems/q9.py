# Search in a 2D matrix
"""
3 ideas (no. 3 was used in the code) :
1. look for the target in matrix element by element. Brute force.
2. Binary search the first row to find the element.If not found, repeat the same with next row until found.
3.
*save indices of top-right-most item in the matrix, call it i,j.
while indices i,j are within bounds, ie, i<length(matrix)-1 & j>=0
*if this matrix[i][j] < target, move i+=1 ie. next row same column (going vertically top to bottom)
*if this matrix[i][j] > target, move j-=1 ie. same row prev column (going horizontally right to left)
*if this matrix[i][j] == target. save the index i,j
return index if found...
"""
from q8 import print_matrix


def lookup(matrix, target):
    i, j = 0, len(matrix[0])-1
    found = False
    while found is not True:
        if matrix[i][j] == target:
            found = True
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        if i > len(matrix)-1 or j <= -1:
            break
    if found:
        return [i, j]
    else:
        return ["Not Found"]


if __name__ == "__main__":
    my_matrix = [[1,  3,   5, 7],
                 [10, 11, 16, 20],
                 [23, 30, 34, 60],
                 [66, 63, 70, 99]
                 ]
    target = 63
    found_index = lookup(my_matrix, target)
    print("Lookup Matrix:")
    print_matrix(my_matrix)
    print(f"\nTarget to find- {target}\nTarget location in matrix- {found_index}")