user_enter_amount_purchase = input("Enter the amount you want to purchase: ")
amount= 1000

if user_enter_amount_purchase.isdigit():
    user_enter_amount_purchase = int(user_enter_amount_purchase)
    if user_enter_amount_purchase > amount:
        print("You got the discout 5%.")
        discount = user_enter_amount_purchase * 0.05
        print(f"Your discount is {discount}.")
        total_amount = user_enter_amount_purchase - discount
        print(f"Your total amount after discount is {total_amount}.")
    else:
        print("You did not get the discount.")
        total_amount = user_enter_amount_purchase
        print(f"Your total amount is {total_amount}.")

    
    
