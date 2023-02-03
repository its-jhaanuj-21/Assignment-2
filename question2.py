# Write a program to accept the cost price of bike and display the road tax to be paid

def calculate_road_tax(cost_price):
    if cost_price > 100000:
        return 0.15 * cost_price
    elif cost_price > 50000:
        return 0.1 * cost_price
    else:
        return 0.05 * cost_price
cost_price = float(input("Enter cost price: "))
road_tax = calculate_road_tax(cost_price)
print("The road tax for a bike with cost price {} is {}".format(cost_price, road_tax))
