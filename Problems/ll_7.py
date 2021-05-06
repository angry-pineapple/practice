# Delete a given Node when a node is given. (0(1) solution)

from ll_1 import LinkList, node
import sys
"""
logic:
overwrite the value in node to be deleted with the value of next node, move right and repeat.
Keep overwriting till we reach end

@TODO:
if last node is given to be deleted, then there's an issue -- fix it.
"""


class ExtendedLinkList(LinkList):
    def __init__(self):
        super(ExtendedLinkList, self).__init__()

    def get_ith_node(self, i):
        temp = self.head
        j = 0
        while(temp!=None and j != i):
            temp=temp.next
            j+=1
        return temp

    def delete_node(self, node):
        temp = node
        if temp.next is not None:
            temp.val = temp.next.val
            temp.next = temp.next.next
        else:
            pass      # rectify here. [If last node is given]



if __name__ =="__main__":
    my_ll = ExtendedLinkList()
    ll_node_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for val in ll_node_vals:
        my_node = node(val)
        current_head = my_ll.append_node(my_node)

    head = my_ll.get_head()
    my_ll.print_ll(head)
    print("\nPlease enter index to delete:",end=" ")
    index = int(input())
    if index >= my_ll.length():
        print("Index out of bounds!!")
        sys.exit()
    node_to_delete = my_ll.get_ith_node(index)
    print('\nNode to delete-[', node_to_delete, f'] ...at index={index}, Node-value-[', node_to_delete.val, ']')
    my_ll.delete_node(node_to_delete)
    head = my_ll.get_head()
    print("After deletion-")
    my_ll.print_ll(head)
