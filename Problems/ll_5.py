#Remove n-th node from the end, of a link list

from ll_1 import LinkList,node

class extended_LinkList(LinkList):
    def __init__(self):
        super(extended_LinkList, self).__init__()

    def remove_n_from_end(self,index_from_end):
        ptr1, ptr2 = self.head,self.head
        print(f"\nremoving {index_from_end}th from the end")
        for i in range(index_from_end):
            ptr2 = ptr2.next
        while ptr2.next!= None:
            ptr1= ptr1.next
            ptr2 = ptr2.next

        # print(ptr1.val, ptr2.val)
        #removing
        node_to_remove = ptr1.next
        print(f"node to remove - {node_to_remove.val}")
        # if node_to_remove == self.head:
        #     temp = self.head
        #     self.head = self.head.next
        #     temp.next = None
        #     return self.head
        next_of_node_to_remove = node_to_remove.next
        node_to_remove.next = None
        ptr1.next = next_of_node_to_remove
        return self.head

if __name__ == "__main__":
    ll1_items = [1,4,6,8,9]
    ll1 = extended_LinkList()
    for item in ll1_items:
        ll_node = node(item)
        head_1 = ll1.append_node(ll_node)

    print("First Linklist //-",end=" ")
    ll1.print_ll(head_1)
    new_head = ll1.remove_n_from_end(5)
    ll1.print_ll(new_head)
