# Tower of Hanoi

def toh(n, source, destination, helper):
    # if 3 disks-
    if n == 0:
        return
    toh(n-1, source, helper, destination)
    print(f"moving disk {n} to --> {destination}")
    toh(n-1, helper, destination, source)

def toh_stack(source, destination, helper):
    if source == []:
        return
    # [1,2,3] [] []
    # [1,2] [] []
    # [1] [] []
    # [1*, 2] [] [1]
    # [1*, 2*] [2] [1]
    # [1* 2*] [2,1] []
    # [1*,2* 3] [2, 1] []
    # [1* 2 * 3*] [2, 1] [3]
    # [1* 2 * 3*] [ 3, 2, 1] []
    toh_stack(source[:-1])

if __name__ == "__main__":
    number_of_disks = 3
    # A,B,C=[],[],[]
    source, helper, destination = 'source', 'helper', 'destination'
    # toh(number_of_disks, source, destination, helper)
    s, d, h = [1, 2, 3], [], []

    a,b,c = toh_stack(s, d, h)
    print(a,b,c)
