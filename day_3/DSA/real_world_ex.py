class Node:
    def __init__(self, data):
        self.data = data      # This will hold the color name (e.g., "GREEN")
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            newNode.next = self.head
        else:
            current = self.head
            # Teacher's logic: Find the node that points back to head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
            
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Loops back to start)")

    # Real-world addition: Simulate the traffic light cycles changing
    def run_traffic_system(self, total_cycles):
        if not self.head:
            print("Traffic system offline!")
            return
            
        current = self.head
        print(f"\n🚦 Starting Traffic System Simulation ({total_cycles} changes):")
        
        for i in range(total_cycles):
            print(f"Signal is: 【 {current.data} 】")
            current = current.next # Moves endlessly through Green -> Yellow -> Red -> Green...

# --- Testing the Real-World Code ---

traffic_signals = CircularLinkedList()

# Append the light colors using your teacher's method
traffic_signals.append("GREEN")
traffic_signals.append("YELLOW")
traffic_signals.append("RED")

# 1. Show the structural connection using your teacher's traverse method
print("--- Structural View ---")
traffic_signals.traverse()

# 2. Simulate it working endlessly in real life
traffic_signals.run_traffic_system(7)
