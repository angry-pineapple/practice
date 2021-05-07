# Add two numbers as LinkedList
"""
logic:
have a dummy node. have a temp node point to this dummy node.
call both linklists - ll1,ll2
traverse both the input linked list WHILE ll1 is not None OR ll2 is not None.
keep adding the values from both ll nodes, break them to find sum digit & carry
make temp point to this sum digit.
(Keep repeating till inside while loop)

finally if there's a carry, make temp point to a node(with carry as value).
return dummy's next
"""
from ll_1 import LinkList, node

class ExtendedLinkList(LinkList):
    def __init__(self):
        super(ExtendedLinkList, self).__init__()

    def add_linklists(self, ll1, ll2):
        dummy = node(0)
        temp = dummy
        carry = 0
        while ll1 is not None or ll2 is not None:
            if ll1 is None:
                digit_sum = ll2.val + carry
            elif ll2 is None:
                digit_sum = ll1.val + carry
            else:
                digit_sum = ll1.val+ll2.val + carry
            digit = digit_sum % 10
            carry = digit_sum//10
            temp.next = node(digit)
            temp = temp.next
            if ll1 is not None:
                ll1 = ll1.next
            if ll2 is not None:
                ll2 = ll2.next
        if carry >= 0:                  # add any remaining carry
            temp.next = node(carry)


        return dummy.next


if __name__ == "__main__":
    number1 = [9,9,9,9,9,9,9]
    number2 = [9,9,9,9]
    num1_ll = ExtendedLinkList()
    num2_ll = ExtendedLinkList()
    for digit in number1:
        digit_node = node(digit)
        num1_head = num1_ll.append_node(digit_node)

    for digit in number2:
        digit_node = node(digit)
        num2_head = num2_ll.append_node(digit_node)
    print("   ",end=" ")
    num1_ll.print_ll(num1_head)
    print("\n  + ",end="")
    num2_ll.print_ll(num2_head)
    print("")
    sum_head = num1_ll.add_linklists( num1_head, num2_head)
    print("    ____________")
    print("   ",end=" ")
    num1_ll.print_ll(sum_head)


