# Majority Element 2 --- > elements occurring MORE than floor(n/3) times.
"""
idea:
Since majority is defined as no occuring more than floor(n/3) times,
we will have 2 majority candidates

count1,count2 = 0,0
candidate1, candidate2 = -1,-1

traverse the items in array:
    if item == candidate1: count1 += 1   [if item is same as candidate, increment count1]
    elif item ==candidate2: count2 += 1  [if item is same as candidate, increment count2]
    elif count1 == 0: candidate1=item    [if count1 becomes 0, make this item as new candidate1]
    elif count2 == 0: candidate2=item    [if count2 becomes 0, make this item as new candidate2]
    else count1 -=1                      [If a new number not matching candidate1 or 2 comes, decrement count1,count2]
         count2 -=1

return candidate1,candidate2
"""
import math


def get_majority_elem(arr):
    count1 = 0
    count2 = 0
    candidate1 = -1
    candidate2 = -1
    for item in arr:
        if item == candidate1:
            count1 += 1
        elif item == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = item
        elif count2 == 0:
            candidate2 = item
        else:
            count1 -= 1
            count2 -= 1

    return [candidate1, candidate2]


if __name__ == "__main__":
    arr = [5, 5, 5, 3, 3, 2, 2]
    candidate_majority_elements = get_majority_elem(arr)
    print(f"My arr- {arr}")
    print(f"majority element- {candidate_majority_elements}")
    n = len(arr)
    n = n / 3
    n = math.floor(n)
    count1, count2 = 0, 0

    for val in arr:
        if val == candidate_majority_elements[0]:
            count1 += 1

    for val in arr:
        if val == candidate_majority_elements[1]:
            count2 += 1

    if count1 > n:
        print(f"Candidate 1 --->{candidate_majority_elements[0]} is a majority element")
    else:
        print(f"Candidate 1 --->{candidate_majority_elements[0]} is NOT a majority element")

    if count2 > n:
        print(f"Candidate 2 --->{candidate_majority_elements[1]} is a majority element")
    else:
        print(f"Candidate 2 --->{candidate_majority_elements[1]} is NOT a majority element")

