queue = []

while True:
    print("enter 1 to enqueue")
    print("enter 2 to dequeue")
    print("enter 3 to peek")
    print("enter 4 to isempty")
    print("enter 5 to size")
    print("enter 6 to exit")
    
    print("enter you option is actiavte operation")
    choice = input("enter your choice: ")
    
    match choice:
        case "1":
            new_item = input("enter the item: ")
            if new_item:
                queue.append(new_item)
                print(new_item," successfully added")
            else:
                print("Product name cannot be empty!")
        
        case "2":
            popedElement =queue.pop(0)
            print("Dequeue:",popedElement)
                    
        case "3":
            frontelement = queue[0]
            print("PEEK",frontelement)
                    
        case "4":
            isempty = not bool(queue)
            print("is empty:",isempty)
                    
        case "5":
            size =len(queue)
            print("size of queue:",size)
                    
        case "6":
            print("thank you")
            break
        