# Define a dictionary to hold the items in the cart, with each item's quantity and price
cart = {}

# Define a function to add an item to the cart
def add_item(item, quantity, price):
    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"quantity": quantity, "price": price}
    print(f"{quantity} {item.capitalize()} added to cart.")

# Define a function to remove an item from the cart
def remove_item(item):
    if item in cart:
        del cart[item]
        print(f"{item.capitalize()} removed from cart.")
    else:
        print(f"{item.capitalize()} not in cart.")

# Define a function to show the current contents of the cart
def show_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        output = []
        for item in cart:
            output.append(f"{item.capitalize()}: {cart[item]['quantity']} x {cart[item]['price']} = {cart[item]['quantity'] * cart[item]['price']:.2f}")
        print("Your cart:\n" + "\n".join(output))

# Define a function to calculate the total price of the items in the cart
def calculate_total():
    total = 0
    for item in cart:
        total += cart[item]["quantity"] * cart[item]["price"]
    return total

# Main program loop
while True:
    print("\nMenu:\n1. Add item to cart\n2. Remove item from cart\n3. View cart\n4. Checkout\n5. Quit")
    choice = input("Enter choice (1-5): ")
    if choice == "1":
        item = input("Enter item name: ").lower()
        if item == "banana":
            price = 0.25
        elif item == "watermelon":
            price = 3.99
        elif item == "strawberry":
            price = 2.99
        elif item == "elderberry":
            price = 4.99
        elif item == "raspberry":
            price = 3.49
        elif item == "blueberry":
            price = 2.99
        elif item == "grapes":
            price = 1.99
        elif item == "apple":
            price = 0.99
        elif item == "frozen breakfast":
            price = 5.99
        elif item == "frozen dinners":
            price = 3.99
        elif item == "kale":
            price = 1.49
        elif item == "spinach":
            price = 1.99
        elif item == "cheese":
            price = 2.99
        elif item == "ground beef":
            price = 5.99
        elif item == "pasta":
            price = 1.99
        elif item == "steak":
            price = 12.99
        else:
            print("Invalid item. Please try again.")
            continue
        quantity = input("Enter quantity (default 1): ")
        if quantity.isdigit():
            quantity = int(quantity)
        else:
            quantity = 1
        add_item(item, quantity, price)
    elif choice == "2":
        item = input("Enter item name: ").lower()
        remove_item(item)
    elif choice == "3":
        show_cart()
    elif choice == "4":
        total = calculate_total()
        print(f"Total price: ${total:.2f}")
       
