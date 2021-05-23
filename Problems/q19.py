# Tower of Hanoi

def toh(n, source, destination, helper):
    # if n == 0:
    #     return
    # toh(n-1, source, helper, destination)
    # print(f"moving disk {n} to --> {destination}")
    # toh(n-1, helper, destination, source)
    if n>0:
        toh(n - 1, source, helper, destination)
        print(f"moving disk {n} to --> {destination}")
        toh(n - 1, helper, destination, source)

def toh_stack(n,start, destination, helper):
    if n > 0:
        toh_stack(n - 1, start, helper, destination)
        destination.append(start.pop())
        toh_stack(n - 1, helper, destination, start)


if __name__ == "__main__":
    number_of_disks = 3
    source, helper, destination = 'source', 'helper', 'destination'
    print("##### Steps ######################")
    toh(number_of_disks, source, destination, helper)
    s, d, h = [3,2,1], [], []
    print("###################################")
    print("\n######### Using stack/array: #####")
    print("before->",s,d,h)
    toh_stack(len(s),s, d, h)
    print("after-> ",s,d,h)
    print("###################################")

