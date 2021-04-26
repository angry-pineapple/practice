"""
Merge two sorted Arrays without extra space
"""

def sort(arr1,arr2):
    ptr1,ptr2 =0,0
    while ptr1<len(arr1):
        if arr1[ptr1]<arr2[ptr2]:
            ptr1 +=1
        else:
            arr1[ptr1],arr2[ptr2] = arr2[ptr2],arr1[ptr1]
            arr2.sort()
    return arr1, arr2


if __name__ == "__main__":
    arr1 = [1, 3, 4, 6]
    arr2 = [2, 8, 5, 7 , 9, 10, 11 ,15]
    print(f"Original array1={arr1}, Original array2={arr2}")
    sorted_array = sort(arr1, arr2)
    print(f"sorted arrays={sorted_array}")