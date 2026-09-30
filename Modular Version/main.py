from menu import display_menu
from order import create_order
from payment import process_payment


print("===================================")
print("   WELCOME TO OUR RESTAURANT")
print("===================================")

display_menu()

choice = int(input("\nEnter your order (1-5): "))
quantity = int(input("Enter quantity: "))

item, total = create_order(choice, quantity)

if total == 0:
    print("Invalid choice!")
else:
    print("You ordered", item)

    print("\n===================================")
    print("          ORDER SUMMARY")
    print("===================================")

    print("Total Amount: PHP", total)

    process_payment(total)