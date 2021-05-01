#Merge 2 sorted linked_list
"""
idea:
get head pointers to both sorted linklist, call it h1, h2
create a new dummy node. Make merged_head point to this dummy node
while h1 and h2 are not None:
if h1<h2 => dummy.next = h1 ; move dummy to the right, move h1 to the right
if h2<h1 => dummy.next = h2 ; move dummy to the right, move h2 to the right

If h1 reaches None first, add all remaining from second link list to the dummy linklist
If h2 reaches None first, add all the remaining from first link list to the dummy linklist
return merged_head
"""
from ll_1 import LinkList,node

class extended_LinkList(LinkList):
    def __init__(self):
        super(extended_LinkList, self).__init__()

    def merge(self,head1,head2):
        dummy = node("[BEGIN]")
        merged_head = dummy
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                dummy.next = head1
                dummy = dummy.next
                head1=head1.next
            else:
                dummy.next = head2
                dummy= dummy.next
                head2 = head2.next

        if head1 == None:
            dummy.next = head2
        if head2 == None:
            dummy.next = head1
        return merged_head

if __name__ == "__main__":
    ll1_items = [1,4,6,6,8,9]
    ll2_items = [2,6,8,10]
    ll1 = extended_LinkList()
    ll2 = extended_LinkList()
    for item in ll1_items:
        ll_node = node(item)
        head_1 = ll1.append_node(ll_node)
    for item in ll2_items:
        ll_node = node(item)
        head_2 = ll2.append_node(ll_node)
    print("First Linklist //-",end=" ")
    ll1.print_ll(head_1)
    print("\n")
    print("Second Linklist //-",end=" ")
    ll2.print_ll(head_2)
    print("\n")
    ll3 = extended_LinkList()
    print("Merged Linklist -", end= " ")
    head_3 = ll3.merge(head_1,head_2)
    ll3.print_ll(head_3)

