class Item:
    def __init__(self, item_id, name, desc, price):
        #error handling
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.item_id = item_id
        self.name = name
        self.desc = desc
        self.price = price

    def __str__(self):
        return "ID " + str(self.item_id) + "\n" + "Description: " + self.desc + "\n" + "Price: " + format(self.price, ".2f") + " Pesos"


class Manager:
    def __init__(self):
        self.items = {}
        self.id = 1
    
    def create(self, name, desc, price):
        try:
            item = Item(self.id, name, desc, price)
            self.items[self.id] = item
            self.id += 1
            print("Item added successfully!")
        except ValueError as e:
            print("Error: " + str(e))
    
    def view(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update(self, item_id, name=None, desc=None, price=None):
        if item_id not in self.items:
            print("Error: Item ID not found.")
            return
        
        item = self.items[item_id]
        
        if name:
            item.name = name
        if desc:
            item.desc = desc
        if price is not None:
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            item.price = price
        
        print("Item updated successfully!")
    
    def delete(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item ID not found.")

#to be able to access the menu options
manager = Manager()
    
while True:
    print("\n==== ITEM MANAGEMENT SYSTEM ====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    print()
    
    if choice == "1":
        name = input("Enter item name: ").strip()
        description = input("Enter item description: ").strip()
        try:
            price = float(input("Enter item price: "))
            manager.create(name, description, price)
        except ValueError:
            print("Error: Price must be a valid number.")
            
    elif choice == "2":
        manager.view()
    
    elif choice == "3":
        try:
            item_id = int(input("Enter item ID to update: "))
            name = input("Enter new name (leave empty to keep current): ").strip()
            description = input("Enter new description (leave empty to keep current): ").strip()
            price_input = input("Enter new price (leave empty to keep current): ")
            #else none will leave the current data in
            price = float(price_input) if price_input else None
            manager.update(item_id, name if name else None, description if description else None, price)
        except ValueError:
            print("Error: Invalid input.")
            
    elif choice == "4":
        try:
            item_id = int(input("Enter item ID to delete: "))
            manager.delete(item_id)
        except ValueError:
            print("Error: Invalid ID format.")
            
    elif choice == "5":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
