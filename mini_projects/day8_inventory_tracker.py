# ---------------------------------------
# 🧩 Mini Project: Inventory Tracker
# ---------------------------------------

# Step 1: Initialize the inventory
inventory = {
    "apple": {"price": 0.99, "quantity": 10},
    "banana": {"price": 0.75, "quantity": 5},
    "orange": {"price": 0.85, "quantity": 8}
}

# Step 2: Function to display inventory
def show_inventory():
    print("\n📦 Current Inventory:")
    print("-------------------------")
    for item, details in inventory.items():
        print(f"{item.title()} - ${details['price']:.2f} (Qty: {details['quantity']})")
    print("-------------------------")

# Step 3: Function to add new item
def add_item():
    item = input("Enter item name: ").lower()
    if item in inventory:
        print("Item already exists. Updating quantity instead.")
        add_quantity(item)
        return
    try:
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter quantity: "))
        inventory[item] = {"price": price, "quantity": quantity}
        print(f"{item.title()} added successfully!")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers for price and quantity.")

# Step 4: Function to update quantity
def add_quantity(item=None):
    if not item:
        item = input("Enter item name to update: ").lower()
    if item not in inventory:
        print("❌ Item not found.")
        return
    try:
        qty = int(input("Enter quantity to add: "))
        inventory[item]["quantity"] += qty
        print(f"✅ {qty} {item}(s) added successfully!")
    except ValueError:
        print("⚠️ Invalid number entered.")

# Step 5: Function to remove item
def remove_item():
    item = input("Enter item name to remove: ").lower()
    if item in inventory:
        del inventory[item]
        print(f"🗑️ {item.title()} removed from inventory.")
    else:
        print("❌ Item not found.")

# Step 6: Main loop
def main():
    while True:
        print("\n=== Inventory Tracker Menu ===")
        print("1. Show Inventory")
        print("2. Add Item")
        print("3. Update Quantity")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            add_quantity()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Step 7: Run program
if __name__ == "__main__":
    main()
