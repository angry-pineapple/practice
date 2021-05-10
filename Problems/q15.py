# Find if there is subarray with zero sum
"""
idea:
say array is -- 1,2,3,-5,1,8,-8
calculate running sum:
sum: 1 3 6  1 2 10 2 6  0
arr: 1 2 3 -5 1 8 -8 4 -6
ind: 0 1 2  3 4 5  6 7  8

if we have 0 or repeating numbers in running sum, we have a subarray with zero sum
in our example:
we have same number 1 & 2 at indexes 0, 3, ..., 4, 6. [thus, (1 to 3) and (5 to 6) will have a zero subarray]
We also have 0 at index 8
therefore subarrays are-
[2, 3, -5] index (from 1 to 3)
[5,6]      index (from 5,6)
[entire array] ..index [0,1,2,3,4,5,6,7,8] {since 0 at index 8}



"""



def subarray_with_zero_present(arr):
    index_sum_arr =[]
    sum,i = 0,0
    for val in arr:
        sum +=val
        index_sum_arr.append([sum,i])
        i+=1
    # for val in index_sum_arr:
    #     print(val[0],end=" ")
    # print("")
    # for val in index_sum_arr:
    #     print(val[1],end=" ")

    dummy_arr=[]
    for val in index_sum_arr:
        # print(val[0],end=" ")
        if val[0]==0:
            return True
        if val[0] in dummy_arr:
            return True
        else:
            dummy_arr.append(val[0])
    return False


if __name__ == "__main__":
    array = [1,2,3,4,5,-15]
    print(f"Array - {array}")
    zero_sum_present = subarray_with_zero_present(array)
    print(f"\nZero sum present? -- {zero_sum_present}")