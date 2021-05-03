#Find intersection point of Y linked-list

"""
Logic(no. 3 was used):
1.  double loop, pick item from linklist1, compare with all items from linklist2.
    Do this for all items in linklist1
2.  Give an attribute to the nodes, called "visited", and set this whenever traversing a node
    Traverse the other linklist, if a node is found whose "visited" value is already set, it means
    that is the intersecting node
3.  Get the head pointers of both linklists- h1,h2
    get length of both linklists- len1, len2.
    calculate the difference abs(len1-len2), call it diff
    move the h1 by 'diff' units. Both, h1 and h2 now have to travel the same distance to reach the end
    Keep moving h1& h2 by 1 unit until h1 == h2
"""
from ll_1 import LinkList,node
class extended_LinkList(LinkList):
    def __init__(self):
        super(extended_LinkList, self).__init__()

    def merge_nodes(self,node1,node2):
        new_node= node("[Common-Node]")
        new_node.next= None
        node1.next = new_node
        node2.next = new_node
        return new_node

    def get_merged_node(self,head1,head2):
        length1 = self.length(head1)
        length2 = self.length(head2)
        diff = abs(length1-length2)
        ptr1 = head1
        ptr2 = head2
        if length1>length2:
            for i in range(diff):
                ptr1 = ptr1.next
        elif length2 > length1:
            for i in range(diff):
                ptr2 = ptr2.next
        while (ptr1 != ptr2):
            if ptr1 == None or ptr2 == None:
                return None
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1



if __name__ == "__main__":
    ll1 = [1,2,3,4,5]
    ll2= ['a','b','c','d','e','f']
    nodes_1 = []
    nodes_2 = []
    linklist1 = extended_LinkList()
    linklist2 = extended_LinkList()
    for item in ll1:
        item_node = node(item)
        head1 = linklist1.append_node(item_node)
        last_added_node_1 = linklist1.last_added_node

    for item in ll2:
        item_node = node(item)
        head2 = linklist2.append_node(item_node)
        last_added_node_2 = linklist2.last_added_node

    print(f"Last added node in ll1={last_added_node_1.val}, & in ll2={last_added_node_2.val}")
    # print("Merging here")
    # linklist_merged = extended_LinkList()
    merged_node = linklist1.merge_nodes(last_added_node_1,last_added_node_2)

    # print(f"LL1 = {last_added_node_1.val}=>{last_added_node_1.next.val},\nLL2 = {last_added_node_2.val}==>{last_added_node_2.next.val}")
    # print("Appending some nodes after merged node")
    # print(f"Merged_node = {merged_node.val}")
    temp = merged_node
    for i in range(90,100):
        new_node = node(i)
        temp.next = new_node
        temp = temp.next
    linklist1.print_ll(head1)
    length1 = linklist1.length()
    print(f"\nLinklist1 length = {length1}")
    linklist1.print_ll(head2)
    length2 = linklist2.length()
    print(f"\nLinklist2 length = {length2}")

    merge_node = linklist1.get_merged_node(head1,head2)
    print(f"The merged node is -{merge_node.val}")
