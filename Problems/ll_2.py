# Reverse linklist

from ll_1 import LinkList,node


class extended_LinkList(LinkList):
    def __init__(self):
        super(extended_LinkList, self).__init__()
        print("--done init--")

    def reverse(self,node):
        if node.next is None:
            self.head = node #make the last node as head
            return node
        else:
            reversed_node = self.reverse(node.next)
            # print(f"returned- {reversed_node.val}")
            # print(f"current node is - {node.val}")
            reversed_node.next = node
            return node

    def reverse_ll(self,head):
        reversed_ll = self.reverse(head)  # we will get the original array's first element.
                                          # Make it point to None since it's the tail now.
        reversed_ll.next = None
        return self.head


if __name__ == "__main__":
    my_ll_elements = [1,2,3,4,5,6,7,8,9,0]
    my_ll = extended_LinkList()
    for val in my_ll_elements:
        ll_node = node(val)
        my_ll_head = my_ll.append_node(ll_node)

    print(f"My Original Linklist=",end = " ")
    my_ll.print_ll(my_ll_head)
    new_head = my_ll.reverse_ll(my_ll_head)
    print(f"\nMy Reversed Linklist=", end  = " " )

    my_ll.print_ll(new_head)
