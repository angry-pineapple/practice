# Majority Element --- > elements occurring MORE than floor(n/2) times.
"""
Ideas:
1. check count of each element one by one - O(n^2)
2. Sort the array, check middle element.
3. Use a hashmap. Go through the array once, keeping a count of all unique values encountered
    O(n), but uses extra space for hashmap

4. Moore's Voting Algorithm:

    step 1: find the candidate majority element
    step 2: verify if that element is in fact the majority element ie., occurs more than floor(n/2) times.

    For step 1:
    init-- count = 1, candidate_majority_element= arr[0] ie., the first element
    for (arr[1:]) :
        if count ==0 :
            we make current item as the new candidate_majority_element
            ie., candidate_majority_element = item
        check if the current item is same as our candidate_majority_element:
        if it is, increase the count by one
        else, if current item is different than our candidate_majority_element:
        if it is, decrease the count by one.
    the candidate_majority_element would be the candidate.

    For Step 2:
    Do a simple array traversal to find out the count of candidate_majority_element
    if it is > floor(n/2) => Then this candidate is in fact, our majority element.

    **IMPORTANT**
    realise that if majority element is said to be floor(n/2), there can ONLY BE ONE candidate majority element
    However, if majority element is said to be floor(n/3), there will be ONLY TWO candidate majority elements
    for first, take the array [ 1 ] as example.
    n = 1, n/2 = 0. ie., the number must occur more than 0 times
    we have 1 such candidate

    for second, take the array [1, 1] as example:
    n = 2, n/3= 0. ie., the number must occur more than 0 times
    we have 2 such candidates

"""
def get_majority_elem(arr):
    count = 1
    candidate = arr[0]
    for item in arr[1:]:
        if count == 0:
            candidate = item
        if item == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == "__main__":
    arr= [5, 1, 4, 5, 4, 4, 1, 4, 5, 5, 5]
    majority_element = get_majority_elem(arr)
    print(f"My arr- {arr}")
    print(f"majority element- {majority_element}")