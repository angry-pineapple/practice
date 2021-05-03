"""
Link list
"""
from sys import stdout


class node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkList():
    def __init__(self):
        self.head = None
        self.last_added_node =None

    def get_head(self):
        return self.head

    def print_ll(self,head):
        while (head !=None):
            value = head.val
            value = str(value)
            print(value,end="==>")
            head = head.next

    def length(self,starting_point =None):
        if starting_point ==None:
            starting_point = self.head
        length =0
        while(starting_point!=None):
            length+=1
            starting_point = starting_point.next
        return length

    def append_node(self,node):
        if self.head == None:
            self.head = node
            return
        temp = self.head
        while(temp.next!= None):
            temp = temp.next
        temp.next = node
        self.last_added_node = node
        return self.head

if __name__ == "__main__":
    linklist_elements = [1,2,3,4,5,6,7]
    my_linklist = LinkList()
    for items in linklist_elements:
        ll_node = node(items)
        my_linklist_head = my_linklist.append_node(ll_node)

    my_linklist.print_ll(my_linklist_head)
