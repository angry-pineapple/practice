#Merge 2 sorted linked_list

from ll_1 import LinkList,node

class extended_LinkList(LinkList):
    def __init__(self):
        super(extended_LinkList, self).__init__()
        print("-Done init-")

    def merge(self,head1,head2):
        while head1 != None and head2 !=None:
            if head1.val<head2.val:
                self.append_node(head1)
                head1=head1.next
            else:
                self.append_node(head2)
                head2.next

        if head1 == None:
            self.append_node(head2)
        if head2 == None:
            self.append_node(head1)
        return self.head

if __name__ == "__main__":
    ll1_items = [1,4,6,8,9]
    ll2_items = [2,7,10]
    ll1 = extended_LinkList()
    ll2 = extended_LinkList()
    for item in ll1_items:
        ll_node = node(item)
        head_1 = ll1.append_node(ll_node)
    for item in ll2_items:
        ll_node = node(item)
        head_2 = ll2.append_node(ll_node)

    ll1.print_ll(head_1)
    print("\n")
    ll2.print_ll(head_2)

    ll3 = extended_LinkList()
    head_3 = ll3.merge(head_1,head_2)
    ll3.print_ll(head_3)

