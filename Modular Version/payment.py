def process_payment(total):
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