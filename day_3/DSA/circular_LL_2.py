class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            newNode.next=self.head
        else:
            current=self.head
            
            while current.next!=self.head:
                current=current.next
            current.next=newNode
            newNode.next=self.head
            
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        current=self.head
        while True:
            print(current.data,end="->")
            current=current.next
            if current==self.head:
                break
            
circular_list=CircularLinkedList()

circular_list.append(1)
circular_list.append(2)
circular_list.append(1)

print("traversing circular list:")
circular_list.traverse()