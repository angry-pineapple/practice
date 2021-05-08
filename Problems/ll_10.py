# Rotate a Linked List
"""
idea:
have 2 pointers p1,p2
make them point to first(old beginning) and second elements of the linklist
call times to rotate - to_rotate
move p1 & p2 by one unit for "to_rotate -1 " times

here we have, new_end = p1, & new_beginning = p2

keep moving p2 till we reach the end of the linklist, call it old end
make old_end.next = old_beginning
make self.head = new_beginning
make new_end.next = None

EG:
for i=2
    *                 $
    1, 2, 3, 4, 5, 6, 7
       p1,p2

here,
*   = old beginning
$   = old end
p1  = new_end
p2  = new_beginning

"""

from ll_1 import LinkList, node


class ExtendedLinkList(LinkList):
    def __init__(self):
        super(ExtendedLinkList, self).__init__()

    def rotate_ll_anti_clock(self, head, n):
        if n==0:
            return self.head
        old_beginning = head
        to_rotate = n
        ptr1 = old_beginning
        ptr2 = old_beginning.next
        for x in range(to_rotate-1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        new_end = ptr1                  # new end node
        new_beginning = ptr2            # new beginning node
        while ptr2.next is not None:
            ptr2= ptr2.next
        old_end = ptr2
        self.head = new_beginning      # make head point to new_beginning
        new_end.next = None            # make new_end point to None
        old_end.next = old_beginning   # Stitch old end to old beginning

        return self.head

if __name__ == "__main__":
    ll_items = [1,2,3,4,5,6,7]
    ll = ExtendedLinkList()
    for i in ll_items:
        new_node = node(i)
        cur_head = ll.append_node(new_node)
    times_to_rotate_og = 8
    times_to_rotate = times_to_rotate_og % len(ll_items)  # Handle the case if rotated more times than length of array
    print("My Original Linklist:")
    ll.print_ll(cur_head)
    print(f"\nMy Counter-Clockwise ({times_to_rotate_og} times) Rotated Linklist:")
    rotated_head = ll.rotate_ll_anti_clock(cur_head,times_to_rotate)
    ll.print_ll(rotated_head)