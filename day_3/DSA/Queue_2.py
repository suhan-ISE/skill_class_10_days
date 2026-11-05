# Queue
#a ticket line. whoever comes first gets served first(FIFO).New people join at the back
#Real use: Printer jobs , call centers ,BFS , task schedulers.

queue = []

#push
queue.append('A')
queue.append('B')
queue.append('C')

print("Queue:",queue)

#peek
frontelement = queue[0]
print("PEEK",frontelement)

#Dequeue
popedElement =queue.pop(0)
print("Dequeue:",popedElement)
print("element after Dequeue:",queue)

#isempty
isempty = not bool(queue)
print("is empty:",isempty)

#size
size =len(queue)
print("size of queue:",size)




