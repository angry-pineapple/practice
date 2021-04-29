"""
Merge Overlapping Subintervals

"""
def get_merged_overlapping(stack):
    """
    :param stack:
    :return:
    :logic:
    [Sort the items in original array "A" by increasing order of first elements]
    maintain 1 stack for new merged ranges, call it new_stack
    pick items from original array "A", one by one, call it val
    pop last added item in the new_array, call it popped_val
    check the intersection of val and popped val, create new start and end values based on that
    Then push this new value back in the new_stack
    keep repeating till covered all elements from original array "A"

    """
    new_stack= []
    for val in stack:
        #if new_stack is empty, put the first element there and skip this iteration
        if new_stack == []:
            new_stack.append(val)
            continue
        #pop value from new_stack, create new start and end based on range intersection and put new range back in new_stack
        popped_val = new_stack[-1]
        start, end = 0,0
        if val[0] >= popped_val[0] and val[0]<=popped_val[1]:
            start = popped_val[0]
            if popped_val[1]>=val[1]:
                end = popped_val[1]
            elif popped_val[1]<=val[1]:
                end = val[1]
            new_stack=new_stack[:-1]
            new_vals = [start,end]
            new_stack.append(new_vals)
        else:
            new_stack.append(val)
    return new_stack

if __name__ == "__main__":
    arr = [[1,3],[2,4],[5,9],[6,12],[13,14]]

    merged_arr = get_merged_overlapping(arr)
    print(f"Original array= {arr} [Sorted by first elements in increasing order],\nArray after merging overlapping intervals= {merged_arr}")