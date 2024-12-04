
def calculate_discount(price, discount_percent):
    #Calculates the final price after applying a discount.
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input

price = int(input("Enter the  price of the item: "))
discount_percentage = int(input("Enter the discount percentage: "))

# Calculate the final price

final_price = calculate_discount(price, discount_percentage)

# Print the result

if final_price < price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")