
def display_menu():
    """Displays the main menu options."""
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        # ✅ Call the display_menu function here
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"✅ '{item}' added to the shopping list.")
        
        elif choice == '2':
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the shopping list.")
        
        elif choice == '3':
            # View list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("📭 Your shopping list is currently empty.")
        
        elif choice == '4':
            # Exit
            print("👋 Goodbye! Happy shopping!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
