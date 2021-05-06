#Print matrix in spiral form
from q7 import print_matrix
"""
1,2,3
4,5,6
7,8,9
= 1,2,3,6,9,8,7,4,5
--------------------
Logic:
Key idea- Have 4 boundary pointers- top, bottom, left right
Have a direction variable, 0,1,2,3 denoting left to right, top to bottom, right to left, and bottom to top
while this boundary does not collapse(ie, top<=bottom and left<=right), Keep doing this:
Store values from left to right. increment top. increment direction
Store values from top to bottom. decrement right. increment direction
Store values from right to left. decrement bottom. increment direction
Store values from bottom to top. increment left. increment direction

change direction like 0,1,2,3,0,1,2,3,0,1,2,3...and so on (use mod: dir = (dir+1)%4 )
"""

def spiral(matrix):
    top,bottom,left,right = 0,len(matrix)-1,0,len(matrix[0])-1
    # print(top,bottom,left,right)
    print_matrix(matrix)
    dir = 0 # 0,1,2,3 == right,down,left,up
    spiral_array = []
    while(top<=bottom and left<=right):
        if dir == 0:
            for i in range(left,right+1):
                spiral_array.append(matrix[top][i])
            top+=1
        elif dir == 1:
            for i in range(top,bottom+1):
                spiral_array.append(matrix[i][right])
            right-=1
        elif dir == 2:
            for i in range(right,left-1,-1):
                spiral_array.append(matrix[bottom][i])
            bottom-=1
        elif dir == 3:
            for i in range(bottom, top-1,-1):
                spiral_array.append(matrix[i][left])
            left +=1

        dir = (dir+1)%4
    return spiral_array
if __name__ == "__main__":
    my_matrix = [[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15],
                 [21,22,23,24,25]]

    spiral_arr = spiral(my_matrix)
    print(f"Spiral order-{spiral_arr}")