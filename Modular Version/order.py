from menu import get_price, get_item_name


def create_order(choice, quantity):
    price = get_price(choice)
    item = get_item_name(choice)

    if price == 0:
        return item, 0

    total = price * quantity
    return item, total