#DOUBLELY LINKED LIST

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
def Traverse(head):
    currentnode = head
    while currentnode:
        print(currentnode.data, end="<->")
        currentnode = currentnode.next
    print("null")
        
def insert_at_beg(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    head = new_node
    return head
    
head = None
head = insert_at_beg(head,5)
head = insert_at_beg(head,10)
head = insert_at_beg(head,15)
head = insert_at_beg(head,20)
    
Traverse(head)
        
    
    
        