#Stack

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        
    def isempty(self):
        return len(self.stack) == 0 
        
    def pop(self):
        if self.isempty():
            return "stack is empty"
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.isempty():
            return "empty"
        return self.stack[-1]
    
mystack = Stack()

mystack.push('S')
mystack.push('U')
mystack.push('H')

print("Stack:",mystack.stack)
print("pop:",mystack.pop())
print("NEW Stack:",mystack.stack)
print("peek:",mystack.peek())
print("isempty:",mystack.isempty())
print("size:",mystack.size())
        