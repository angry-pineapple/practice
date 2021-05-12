# Subarray with a given sum
"""
idea:
say target = 15
                                      eg-
arr-               0, 1,2,3, 4,        5,          6, 7, 8
running sum arr-   0, 1,3,6,10,        15,         21,28,36
                                ((rs-target)15-15=0)
                                   0 Already present
                                   at 0,
                                   so from 1 to 5
                                   target sum is achieved

have a hashmap
For each item from arr,
calculate current_running_sum, then check if current_running_sum-target is present in hashmap
if present then we have subarray with sum=target from hashmap[current_running_sum-target] +1 to current index
if not present, add hashmap[current_running_sum] = current index

TODO:
 one edge case is not satisfying, fix it.
"""

def get_subarray_with_k_sum(arr, k):
    running_sum_arr = []
    current_sum = 0
    for item in arr:
        current_sum += item
        running_sum_arr.append(current_sum)

    current_sum = 0
    sum_hash = {}
    index = 0
    subarrays = []
    for items in arr:
        current_sum += items
        if index == 0:
            if current_sum ==k:
                start_index = index
                end_index = index
                subarrays.append([start_index, end_index])
            sum_hash[current_sum] = index
        if current_sum - k in sum_hash.keys():
            start_index = sum_hash[current_sum-k] + 1
            end_index = index
            subarrays.append([start_index, end_index])
            sum_hash[current_sum] = index
        else:
            sum_hash[current_sum] = index
        index += 1

    return subarrays

if __name__ == "__main__":
    my_arr = [1, 4, 3, -2, -1, 3, 2, 1,-3]
    # my_arr= [1,2,3,4,5,-15]
    # k= 15   # <-- This edge case isn't handled, handle it.
    k=3
    sub_arr = get_subarray_with_k_sum(my_arr, k)
    print(f"My array- {my_arr}")
    print(f"Target sum required- {k}")
    print(f"Subarray(s) found within indexes- {sub_arr}")

