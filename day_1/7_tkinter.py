import tkinter as tk
from tkinter import simpledialog, messagebox

# 1. Create a hidden main window (required by tkinter)
root = tk.Tk()
root.withdraw()

# 2. Pop up a window asking the question
status = simpledialog.askstring(
    "Status Check", 
    "nim status eli (poor, middle, rich):"
)

# Handle the case where the user clicks 'Cancel'
if status is None:
    messagebox.showinfo("Exit", "Byee!")
else:
    # Clean up the input text just like before
    status = status.strip().lower()

    # 3. Your match-case logic to determine the response
    match status:
        case "poor":
            response = "Mr beast du chaddi toli"
            
        case "middle":
            response = "ooh namavru"
            
        case "rich":
            response = "nim range ast nav ella bidi"
            
        case _:
            response = "Enri media input adu?"

    # 4. Show the result in a nice popup window box
    messagebox.showinfo("Result", response)
