# 2 Sum Problem
"""
idea,
*** This method uses sorting ***
have an array 'P' for storing the indices
sort the array
have 2 pointers left and right, at left index and right most index of the sorted array
now while l<r, check:
        if A[l]+A[r] > sum:
            r -=1
        if A[l]+A[r] < sum:
            l+=1
        if A[l] == A[r] :
            add this index pair [l,r] to some array P
            l+=1, r-=1

return P

TODO
 method 2: using hashing

"""


def get_pair_with_sum(arr,sum):
    left,right  = 0, len(arr)-1
    sorted_arr = sorted(arr)
    print(sorted_arr)
    indices= []
    while left < right:

        if sorted_arr[left]+sorted_arr[right] > sum:
            right -=1
        elif sorted_arr[left]+sorted_arr[right]<sum:
            left+=1
        elif sorted_arr[left]+ sorted_arr[right] == sum:
            indices.append([left,right])
            left += 1
            right -= 1

    return indices

if __name__ == "__main__":
    my_arr = [1, 4, 12,45, 6, 10, -8, 24]
    #sorted = -8, 1, 4, 6, 10,  45
    req_sum = 16

    pair_index = get_pair_with_sum(my_arr,req_sum)
    print(f"pair(s) with sum={req_sum} : {pair_index}")