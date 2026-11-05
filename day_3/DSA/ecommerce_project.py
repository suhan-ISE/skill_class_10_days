# Ecommerce CART project using stack .
# product limit 10 
# operations : push,pop,peek,isempty,view,size.

class EcommerceCart:
    def __init__(self):
        self.cart = []
        
    def push(self,element):
        self.cart.append(element)
        
    def isempty(self):
        return len(self.cart) == 0 
        
    def pop(self):
        if self.isempty():
            return "cart is empty"
        return self.cart.pop()
    
    def size(self):
        return len(self.cart)
    
    def peek(self):
        if self.isempty():
            return "empty"
        return self.cart[-1]
    
mycart = EcommerceCart()


print("--- Welcome to E-commerce Cart ---")



while True:
    print("\noptions:")
    print("1. push     2. pop     3. peek     4. size     5. isempty     6. view     7. exit")
    
   
    choice = input("Enter an number: ")
    
   
    match choice:
        case "1":
            
            if mycart.size() > 10:
                print("Cannot add product! Cart is full (Maximum 10 products allowed).")
            else:
                new_item = input("Enter the product name to add: ").strip()
                if new_item:
                    mycart.push(new_item)
                    print(new_item," successfully added to the cart.")
                else:
                    print("Product name cannot be empty!")
                
        case "2":
            removed_item = mycart.pop()
            print("Removed item:", removed_item)
            
        case "3":
            print("Top item (Peek):", mycart.peek())
            
        case "4":
            print("Total items in cart (Size):", mycart.size())
            
        case "5":
            print(f"Is the cart empty?: {mycart.isempty()}")
            
        case "6":
            print("Current cart items:", mycart.cart)
            
        case "7":
            print("Thank you for using the cart! Goodbye.")
            break
            
        case _:
            print("Invalid option.")




