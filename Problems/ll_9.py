# Detect a cycle in Linked List
"""
[for finding loop, think of hcf concept. minute and hour hand meeting concept.]
idea:

finding the loop- have slow pointer and a fast pointer, slow_ptr & fast_ptr
                  in the beginning point them to head of the linklist
                  increment slow_ptr by 1 unit, & fast_ptr by 2 units
                  if at any point slow_ptr == fast_ptr, there is a loop
                  if fast_ptr reaches end, there is no loop

finding the loop node- save the slow_ptr/fast_ptr[both are pointing to same node btw] in temp2
                       have another variable temp point to head of the linklist
                       while/Until temp reaches the slow_ptr/fast_ptr, increment temp by 1 and temp2 by 1
                       once temp reaches slow_ptr/fast_ptr, temp2 should be the last node in the linklist
                       so looped node is temp2.next

removing the loop node - make temp2.next as None

"""


from ll_1 import LinkList, node


class ExtendedLinkList(LinkList):
    def __init__(self):
        super(ExtendedLinkList,self).__init__()

    def is_loop_present(self,head):
        slow_ptr = head
        fast_ptr = head.next.next
        while True and fast_ptr is not None and fast_ptr.next is not None:
            if slow_ptr == fast_ptr:
                # print(f"Slow_ptr = fast_ptr at- {slow_ptr.val}")
                loop_node = self.find_and_remove_loop_node(head, slow_ptr)
                return True,loop_node
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            # if slow_ptr == fast_ptr:
            #     self.find_loop_node(head,slow_ptr)
            #     return True
        return False,None

    def find_and_remove_loop_node(self,head,slow_ptr):
        temp = head
        temp2 = slow_ptr
        while temp!= slow_ptr:
            temp= temp.next
            temp2 = temp2.next

        loop_node = temp2.next
        print(f"Found that the Linked list was looped to node -{loop_node.val, loop_node}")
        print("Removing the loop")
        temp2.next = None
        return loop_node


if __name__=="__main__":
    ll_items = [1,2,3,4,5]
    ll = ExtendedLinkList()
    loop_index = 1
    i=0
    for val in ll_items:
        node_to_add = node(val)
        cur_head = ll.append_node(node_to_add)
        if i == loop_index:
            loop_node = node_to_add
        i+=1
    print("Original linkedlist= ",end=" ")
    ll.print_ll(cur_head)
    print(f"\nIntroducing a loop from the end of the linked list to index-{loop_index}")
    print("Done")
    print("\n\nNow trying to find and remove the loop")
    temp = cur_head
    while temp.next is not None:
        temp = temp.next
    temp.next = loop_node
    # ll.print_ll(cur_head) # infinite, linkedlist is looped

    loop_node_present, loop_node_found = ll.is_loop_present(cur_head)
    print("Linked list after loop was removed:")
    ll.print_ll(cur_head)
    # if loop_node_present:
    #     loop_node_found = ll.find_loop_node(cur_head)
    #     print(f"Loop node found - {loop_node_found}, value- {loop_node_present.val}")
