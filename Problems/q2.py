"""
Repeat and Missing Number
"""
def get_missing_and_repeating(arr):
    """
    :param arr:
    :return:
    :logic:
    # create an array from 1 to length(arr), call it temp.
    # take the binary representation of the above xor and find an index which is set(set means 1)
    # eg. 1^2^3^1^1^2^3^4 = 5 (1^4) = 0b101 ... (we have to find 1 and 4, call it a&b)
    # therefore from right, 1st index is set
    # this means, for constituent numbers (a&b) the right most bit must be opposite, because 5(0b101) has
    # right most index as set, lets call this index as I
    # So, we create 2 buckets,
    # Put the numbers from "Temp" whose binary representation has 1 at I, in bucket1
    # Put numbers from "Temp" whose binary representation does not have 1 at I, in bucket2
    # Also put the numbers from "arr" whose binary representation has 1 at I, in bucket1
    # And put numbers from "arr" whose binary representation does not have 1 at I, in bucket2
    # Xor both the buckets one by one. We will get the missing and repeating no.
    """
    temp = list(range(1, len(arr)+1))  # array of 1 to N,
    xor = 0
    # arr XOR temp
    for num in arr:
        xor = xor ^ num
    for num in temp:
        xor = xor ^ num
    print(f"xor of arr({arr}) and temp({temp}) => {xor}")

    i, set_index = 1, 0
    bucket1,bucket2= [], []
    for index in range(1,len(bin(xor))):
        if str(bin(xor))[-index] == '1':
            set_index= i
            break
        i+=1

    for i in temp:
        if bin(i)[-set_index] == "1":
            bucket1.append(i)
        else:
            bucket2.append(i)
    # print(f"[Temp],bucket1={bucket1}, Bucket2={bucket2}")

    for i in arr:
        if bin(i)[-set_index]=="1":
            bucket1.append(i)
        else:
            bucket2.append(i)

    # print(f"[Temp+arr]bucket1={bucket1}, Bucket2={bucket2}")
    # Now xor both the buckets, we will get repeating and missing

    xor1, xor2 = 0, 0
    for x in bucket1:
        xor1 = xor1 ^ x
    for x in bucket2:
        xor2 = xor2 ^ x
    return xor1, xor2

if __name__ == "__main__":
    arr = [1,2,3,1]
    a,b= get_missing_and_repeating(arr)
    print(f"Original array-{arr}... Repeating={a}, missing={b}.")