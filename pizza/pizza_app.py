import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_total_price(pizza_qty, pizza_size, burger_qty, burger_size, drinks_qty, extra_cheese, extra_ketchup):
    """Calculate the total price of the order based on quantities and extras selected."""
    prices = {
        "Pizza": {"Small": 5, "Medium": 7, "Large": 10},
        "Burger": {"Classic": 5, "Big": 7},
        "Soft Drink": 2,
        "Extra Cheese": 1,
        "Extra Ketchup": 1
    }

    total = 0
    total += pizza_qty * prices["Pizza"][pizza_size]
    total += burger_qty * prices["Burger"][burger_size]
    total += drinks_qty * prices["Soft Drink"]
    if extra_cheese:
        total += prices["Extra Cheese"]
    if extra_ketchup:
        total += prices["Extra Ketchup"]
    
    return total

def submit_order():
    """Gather user input, calculate total price, and display the order summary."""
    pizza_qty = pizza_quantity_var.get()
    pizza_size = pizza_size_var.get()
    burger_qty = burger_quantity_var.get()
    burger_size = burger_size_var.get()
    drinks_qty = drinks_quantity_var.get()
    order_type = order_type_var.get()
    extra_cheese = extra_cheese_var.get()
    extra_ketchup = extra_ketchup_var.get()

    total_price = calculate_total_price(pizza_qty, pizza_size, burger_qty, burger_size, drinks_qty, extra_cheese, extra_ketchup)

    summary = (
        f"Order Summary:\n"
        f"Pizza: {pizza_qty} x {pizza_size}\n"
        f"Burger: {burger_qty} x {burger_size}\n"
        f"Soft Drinks: {drinks_qty}\n"
        f"Order Type: {order_type}\n"
        f"Extra Cheese: {'Yes' if extra_cheese else 'No'}\n"
        f"Extra Ketchup: {'Yes' if extra_ketchup else 'No'}\n"
        f"Total Price: ${total_price}"
    )
    messagebox.showinfo("Order Summary", summary)

    ## create a file called receipt.txt 
    with open("receipt.txt", "w") as file:
        file.write(summary)


    

# Create the main window
root = tk.Tk()
root.title("Restaurant Menu")


# Labels and entries
tk.Label(root, text="Enter pizza quantity:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
pizza_quantity_var = tk.IntVar()
tk.Entry(root, textvariable=pizza_quantity_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select pizza size:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
pizza_size_var = tk.StringVar(value="Small")
pizza_sizes = ["Small", "Medium", "Large"]
ttk.OptionMenu(root, pizza_size_var, pizza_sizes[0], *pizza_sizes).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter burger quantity:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
burger_quantity_var = tk.IntVar()
tk.Entry(root, textvariable=burger_quantity_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Select burger size:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
burger_size_var = tk.StringVar(value="Classic")
burger_sizes = ["Classic", "Big"]
ttk.OptionMenu(root, burger_size_var, burger_sizes[0], *burger_sizes).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Enter soft drinks quantity:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
drinks_quantity_var = tk.IntVar()
tk.Entry(root, textvariable=drinks_quantity_var).grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Select order type:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
order_type_var = tk.StringVar(value="Takeaway")
tk.Radiobutton(root, text="Takeaway", variable=order_type_var, value="Takeaway").grid(row=5, column=1, padx=10, pady=5, sticky='w')
tk.Radiobutton(root, text="Dine in", variable=order_type_var, value="Dine in").grid(row=5, column=2, padx=10, pady=5, sticky='w')

extra_cheese_var = tk.BooleanVar()
tk.Checkbutton(root, text="Extra Cheese", variable=extra_cheese_var).grid(row=6, column=1, padx=10, pady=5, sticky='w')

extra_ketchup_var = tk.BooleanVar()
tk.Checkbutton(root, text="Extra Ketchup", variable=extra_ketchup_var).grid(row=7, column=1, padx=10, pady=5, sticky='w')

submit_button = ttk.Button(root, text="Order Summary", command=submit_order)
submit_button.grid(row=8, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
