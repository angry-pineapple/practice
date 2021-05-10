# Clone a linked list with Next and Random Pointers
from ll_1 import LinkList
"""
idea:
each node has - [val, next, arbit ] 
4 step process:
1. travel the original linklist and create a mapping (current address: next address) for each node
2. travel the original linklist and 
        for each node create a new clone node having same value
            original linklist's current node's next = new clone node
            make new clone node's arbit = original linklist's current node
    
3.  travel the cloned linklist and
        for each node :  
            current node's arbit = current node's arbit's arbit's next
            
4. use the original hashmap to stitch back the original linklist

            

"""


class node():
    def __init__(self, val, next=None, arbit=None):
        self.val= val
        self.next = next
        self.arbit = arbit

class ExtendedLinkList(LinkList):
    def __init__(self):
        super(ExtendedLinkList, self).__init__()

    def get_ith_node(self, i):
        temp = self.head
        while i > 1:
            temp = temp.next
            i -= 1
        return temp

    def clone_linklist(self,head):
        # create hashmap of original linklist's next
        original_next_hashmap = {}
        temp = head
        while temp is not None:
            current_address = temp
            next_address = temp.next
            original_next_hashmap[current_address]=next_address
            temp = temp.next

        # Create a clone link-list by traversing through the original linklist for values
        # make each node from original linklist(next) point to corresponding node in cloned linklist
        temp = head
        clone_temp = None
        clone_start = None
        while temp is not None:
            cur= temp
            if clone_temp == None:
                new_node = node(temp.val)
                clone_temp= new_node
                clone_start = clone_temp
            else:
                new_node = node(temp.val)
                clone_temp.next = new_node
                clone_temp = new_node
            temp = temp.next
            cur.next = new_node
            new_node.arbit= cur

        original_head_ptr = head
        cloned_head_ptr = clone_start

        while cloned_head_ptr is not None:
            if cloned_head_ptr.arbit.arbit == None:
                cloned_head_ptr.arbit = None
            else:
                cloned_head_ptr.arbit = cloned_head_ptr.arbit.arbit.next
            cloned_head_ptr = cloned_head_ptr.next

        #Stitch back original linklist
        original_head_ptr = head
        cloned_head_ptr = clone_start

        for key,val in original_next_hashmap.items():
            key.next = val

        return [original_head_ptr,cloned_head_ptr]



if __name__ == "__main__":
    ll_values = [1,2,3,4,5,6]
    my_ll = ExtendedLinkList()
    for item in ll_values:
        my_node = node(item)
        cur_head = my_ll.append_node(my_node)
    print("original:", end=" ")
    my_ll.print_ll(cur_head)

    got_node= my_ll.get_ith_node(1)
    arbit_pointer_mapping = {2:4,
                             4:3,
                             5:1}

    temp = my_ll.get_head()
    i = 1
    while temp is not None:
        if i in arbit_pointer_mapping.keys():
            original_node = my_ll.get_ith_node(i)
            arbit_node = my_ll.get_ith_node(arbit_pointer_mapping[i])
            original_node.arbit = arbit_node
        i += 1
        temp = temp.next
    print("\nDone adding arbit pointers")
    print("Arbit mapping:-",arbit_pointer_mapping)
    temp= my_ll.get_head()
    new_linklist = my_ll.clone_linklist(temp)
    print("Done cloning ..")
    print("original:",end=" ")
    print(my_ll.print_ll(new_linklist[0]))
    print("Cloned:  ", end=" ")
    print(my_ll.print_ll(new_linklist[1]))
    cloned_head = new_linklist[1]
    original_head = new_linklist[0]
    print(f"{original_head.next.val} (original_head.next.arbit.val)  ==> {original_head.next.arbit.val}, ... address = {original_head.next.arbit}")
    print(f"{cloned_head.next.val} (cloned_head.next.arbit.val)   ===> {cloned_head.next.arbit.val}, ...   address = {cloned_head.next.arbit}")

