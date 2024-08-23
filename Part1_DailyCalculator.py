

# Define profit margins for each product category
profit_margins = {
    1: 120.45,  # Apple iPhone
    2: 99.50,   # Android Phone
    3: 75.69,   # Apple Tablet
    4: 65.73,   # Android Tablet
    5: 51.49    # Windows Tablet
}

print("Welcome to Circle Phones' Profit calculator.")

# Initialize total profit
total_profit = 0

while True:
    # Ask user to enter product category
    category_input = input("Enter product number 1-5, or enter 0 to stop: ")
    
    # Validate input
    if category_input.isdigit():
        category = int(category_input)
        
        # Check if user wants to stop
        if category == 0:
            break
        # Check if the category is valid
        elif category in profit_margins:
            # Get quantity sold
            quantity_input = input("Enter quantity sold: ")
            if quantity_input.isdigit():
                quantity = int(quantity_input)
                # Calculate profit for this category and add to total profit
                total_profit += profit_margins[category] * quantity
            else:
                print("Invalid input, please enter a valid number")
        else:
            print("Invalid input, please enter a valid number")
    else:
        print("Invalid input, please enter a valid number")

# Print total profit
print(f"Your total profit for today is: {total_profit:.2f}")
