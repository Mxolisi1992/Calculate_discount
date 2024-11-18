O= float(input("Enter the price: "))
discount_percent = int(input("Enter the percentage: "))
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent = discount_percent / 100
        discount = discount_percent * price
        new_price = price - discount
        print(f"The discount is {discount_percent},and new price is ${new_price}.")
    else:
        print(f"The percentage{discount_percent}% is too low, the {price} is the original price.")      


O = float(input("The final price:$"))
D = float(input("The price after the discount:$"))
P = 100/(O/D)
P2 = str(round(P,2))
print("The discount(in percentage) is",P2,"%")



