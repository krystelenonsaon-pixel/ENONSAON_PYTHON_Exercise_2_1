from restaurant import Restaurant


restaurant = Restaurant()

print("===================================")
print("   WELCOME TO OUR RESTAURANT")
print("===================================")

restaurant.display_menu()

choice = int(input("\nEnter your order (1-5): "))
quantity = int(input("Enter quantity: "))

total = restaurant.order(choice, quantity)

if total > 0:
    print("\n===================================")
    print("          ORDER SUMMARY")
    print("===================================")

    print("Total Amount: PHP", total)

    restaurant.payment(total)