def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
    else:
        final_price = price

    print("The final price after applying the discount is:", final_price)


# Values for the original price and discount percentage
original_price = 5000
discount_percentage = 30

# Calling the function
calculate_discount(original_price, discount_percentage)

