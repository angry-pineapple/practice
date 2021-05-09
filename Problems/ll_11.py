# Check if a Linked List is palindrome

"""
idea:
1. Could use a stack
2. without using a stack:

steps:
        our linklist:- 1=>2=>3=>2=>1
        get the middle node:- 3
        reverse the linklist from next of mid till the end. we'll have :
        1=>2=>3=>1=>2
        ^        ^
        now compare nodes from begin to mid with nodes from next of mid till the end
        if mismatch : return False
        else : return True
***
Good to reverse the linklist from next of mid till end (To get the original linklist back),
after comparison is done, but not covered in this code.
***

"""
from ll_1 import LinkList, node


class ExtendedLinkList(LinkList):
    def __init__(self):
        super(ExtendedLinkList, self).__init__()

    def reverse_ll(self,head):
        if head.next == None:
            self.dummy_head = head
            return head
        else:
            reversed = self.reverse_ll(head.next)
            reversed.next = head
            return head

    def reverse(self, head):
        self.dummy_head = head
        reversed_head = self.reverse_ll(head)
        reversed_head.next = None
        return self.dummy_head

    def get_middle(self, head):
        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr= slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr


    def is_palindrome(self,head):
        # Get middle of this linklist
        middle = self.get_middle(head)
        print(f"\nmiddle node is={middle.val}")
        # reverse the linklist from next of middle
        reversed_head = self.reverse(middle.next)
        middle.next = reversed_head
        begin1  = head
        begin2 = reversed_head
        print("After reversing the linklist from next of mid to end of linklist:")
        self.print_ll(begin1)
        print("\nnow we compare nodes from begin till mid, to the nodes from next of mid till end")

        while begin2 is not None:
            if begin1.val == begin2.val:
                begin1 = begin1.next
                begin2 = begin2.next
            else:
                return False
        # Here, Reverse the linklist from mid to end again to get the original linklist back
        return True

if __name__ == "__main__":
    ll_items = [1, 2, 2, 1]
    ll = ExtendedLinkList()
    for i in ll_items:
        n = node(i)
        cur_head = ll.append_node(n)
    ll.print_ll(cur_head)
    isPalindrome = ll.is_palindrome(cur_head)
    print(f"\nThe linklist is palindrome- {isPalindrome}")


