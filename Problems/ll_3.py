# Find middle of LinkedList
from ll_1 import LinkList,node

class extended_LinkList(LinkList):
    def __init__(self):
        super(extended_LinkList, self).__init__()
        print("--done init--")

    def get_mid(self,head):
        """
        :param head:
        :return:
        :logic:
        have 2 pointers, fast_ptr and slow_ptr. Have them point at the head in the beginning
        keep moving slow_ptr by 1 unit and fast_ptr by 2 units.
        By the time fast pointer reaches the end of the linklist, slow_ptr would be at the middle node
        """
        slow_ptr= fast_ptr = head
        while fast_ptr != None and fast_ptr.next!= None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

if __name__ == "__main__":
    my_ll_items = [1,2,3,4,5]
    my_ll = extended_LinkList()
    for item in my_ll_items:
        ll_node = node(item)
        head = my_ll.append_node(ll_node)

    print(f"My LinkList :",end=" ")
    my_ll.print_ll(head)
    print("\nFinding the middle node...")
    head = my_ll.get_head()
    print("Middle node is =",end = " ")
    middle_node = my_ll.get_mid(head)
    print(f"{middle_node.val}")