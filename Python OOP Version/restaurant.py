class Restaurant:

    def __init__(self):
        self.prices = {
            1: 80,
            2: 150,
            3: 120,
            4: 100,
            5: 50
        }

        self.items = {
            1: "Burger",
            2: "Pizza",
            3: "Fried Chicken",
            4: "Spaghetti",
            5: "Soft Drinks"
        }

    def display_menu(self):
        print("\n------------- MENU -------------")
        print("1. Burger        - PHP 80")
        print("2. Pizza         - PHP 150")
        print("3. Fried Chicken - PHP 120")
        print("4. Spaghetti     - PHP 100")
        print("5. Soft Drinks   - PHP 50")
        print("--------------------------------")

    def order(self, choice, quantity):
        if choice in self.prices:
            item = self.items[choice]
            total = self.prices[choice] * quantity

            print("You ordered", item)
            return total

        print("Invalid choice!")
        return 0

    def payment(self, total):
        payment = float(input("Enter payment: PHP "))

        if payment >= total:
            change = payment - total

            print("Payment: PHP", payment)
            print("Change: PHP", change)

            print("\n===================================")
            print("   THANK YOU FOR YOUR ORDER!")
            print("       PLEASE COME AGAIN!")
            print("===================================")

        else:
            balance = total - payment
            print("Insufficient payment!")
            print("Remaining Balance: PHP", balance)