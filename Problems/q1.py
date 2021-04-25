"""
Sort an array of 0’s 1’s 2’s without using extra space or sorting algo
https://www.youtube.com/watch?v=oaVa-9wmpns&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=2 (Problem link in description)
"""
def sort(array):
    """
    :param array: array of 0s,1s,2s
    :return: sorted array of 0s,1s,2s
    :logic:
    3 index-pointers low=0, mid=0 & high= N (last index of array)
    we move move mid till it reaches high.
    everything from 0 to low is 0
    everything from low to mid is 1
    everything from mid to N is 2
    """
    print(f"i/p Array is ={array}")
    low,mid = 0,0
    high= len(array)-1
    while (mid <= high):
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[mid],array[high] = array[high],array[mid]
            high -= 1
    return array


if __name__ == "__main__":
    array = [1,1,2,0,1,2,0,0,0,1,1,1,1,2,2,2,1,1,1]
    sorted_a= sort(array)
    print("Sorted array is {}".format(sorted_a))