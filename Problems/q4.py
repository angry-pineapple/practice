"""
Kadane’s Algorithm
Find the subarray which has the maximum sum
"""
def get_max_subarray_sum(arr):
    """
    :param arr:
    :return:
    :logic:
    have 2 variables, sum_till_now, sum_here.
    keep adding items from array to sum_here, and check
    if sum_here becomes -ve, make sum_till_now = 0
    if sum_here becomes > sum_till_now, then make sum_till_now = sum_here
    """
    max_till_now = 0
    max_here = 0
    sub = []
    s,i=0,0
    for item in arr:
        max_here = max_here + item
        if max_here < 0:
            max_here = 0
            s = i+1
        if max_here > max_till_now:
            max_till_now = max_here
            start = s
            end = i
        i+=1


    print(start, end)
    return max_till_now
if __name__ == "__main__":
    # arr = [2,-10,11,3,4,-5,1]
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(arr)
    sub_arr_sum = get_max_subarray_sum(arr)
    print(f"Max subarray sum= {sub_arr_sum}")