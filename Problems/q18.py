# Trapping Rainwater
"""
idea is very simple,
for each element in the array, we find out how much water will be ON TOP OF THAT ELEMENT.

Lets say for any element at index i, the value is A.
Lets call water on top of this "A" as w.
Therefore,
    w = MIN( MAX(ELEMENTS TO THE LEFT OF i), MAX(ELEMENTS TO THE RIGHT OF i(inclusive) )) - A
    IF w <=0:
       w = 0
    Keep adding w to another array, called "filled_arr"

return sum(filled_arr)

"""


def get_trapped_water(arr):
    water_level = []
    for i in range(len(arr)):
        if i == 0:
            left_max = 0
        else:
            left_max = max(arr[:i])
        right_max = max(arr[i:])
        if arr[i] >= left_max or arr[i] >= right_max:
            water = 0
        else:
            water = min(left_max, right_max) - arr[i]
        if water <= 0:
            water = 0
        water_level.append(water)
    print(f"Structure w/ water- {water_level}")
    return sum(water_level)

if __name__ == "__main__":
    structure =  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # structure = [3, 0, 2, 0, 4]
    water_stored = get_trapped_water(structure)
    print(f"Input structure-    {structure}")
    print(f"Stored water in the i/p structure- {water_stored} units")