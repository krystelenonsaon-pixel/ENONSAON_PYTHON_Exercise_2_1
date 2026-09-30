def display_menu():
    print("\n------------- MENU -------------")
    print("1. Burger        - PHP 80")
    print("2. Pizza         - PHP 150")
    print("3. Fried Chicken - PHP 120")
    print("4. Spaghetti     - PHP 100")
    print("5. Soft Drinks   - PHP 50")
    print("--------------------------------")


def get_price(choice):
    prices = {
        1: 80,
        2: 150,
        3: 120,
        4: 100,
        5: 50
    }

    return prices.get(choice, 0)


def get_item_name(choice):
    names = {
        1: "Burger",
        2: "Pizza",
        3: "Fried Chicken",
        4: "Spaghetti",
        5: "Soft Drinks"
    }

    return names.get(choice, "Invalid choice")