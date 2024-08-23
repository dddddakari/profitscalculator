# Derek Sow :) - Group 16


# Define profit margins for each product category
profit_margins = {
    1: 120.45,  # Apple iPhone
    2: 99.50,   # Android Phone
    3: 75.69,   # Apple Tablet
    4: 65.73,   # Android Tablet
    5: 51.49    # Windows Tablet
}

# Printing the text that welcomes the user
print("Welcome to Circle Phones Profit calculator")
print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
print("Enter:")
print("1 - For specific Day")
print("2 - For the Week")
print("3 - For Week Business Days")
print("4 - For Weekend days")
print("0 - Exit \n")

# Getting the input for the category
while True:
    period_input = input()
    
    # Making sure that the input the user enters MUST be a numeral
    if period_input.isdigit():
        period = int(period_input)
        
        # Exit the program
        if period == 0:
            print("Program End!")
            break
        
        # Handle specific day calculation
        elif period == 1:
            day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ").strip().capitalize()
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            
            # The function that prints the 'For ____' and also the total counter 
            if day in days:
                print(f"For {day}")
                total_profit = 0
                # Entering the product number, making sure it is a digit and assigning it to the category variable
                while True:
                    category_input = input("Enter product number 1-5 or 0 to stop: ")
                    
                    if category_input.isdigit():
                        category = int(category_input)
                        # Making sure to exit if 0 is inputted
                        if category == 0:
                            break
                        # But if the inputted number IS apart of the main dictionary, test to see if it is a digit, add it to the quantity variable and add it to the total
                        elif category in profit_margins:
                            quantity_input = input("Enter quantity sold: ")
                            if quantity_input.isdigit():
                                quantity = int(quantity_input)
                                total_profit += profit_margins[category] * quantity
                            # The invalids to stop user from inputting whatever they want
                            else:
                                print("Invalid input, please enter a valid number")
                        else:
                            print("Invalid input, please enter a valid number")
                    else:
                        print("Invalid input, please enter a valid number")
                
                # Print total profit for the day
                print(f"Total Profit for the {day} is: ${total_profit:.2f}")
                
                # Printing the optional dialogue, depending on if they passed 10k or not
                if total_profit >= 10000:
                    print("You did good this week")
                else:
                    print(f"More hard work needed... The last {day} wasn't the best")
        
        # Handle week calculation -- if 2 is entered
        elif period == 2:
            total_week_profit = 0
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            # Printing the 'For _____' that is seen in the text output 
            for day in days:
                print(f"For {day}")
                day_profit = 0
                # Entering the product number, making sure it is a digit and assigning it to the category variable
                while True:
                    category_input = input("Enter product number 1-5 or 0 to stop: ")
                    
                    if category_input.isdigit():
                        category = int(category_input)
                        # Making sure to exit if 0 is inputted
                        if category == 0:
                            break
                        # But if the inputted number IS apart of the main dictionary, test to see if it is a digit, add it to the quantity variable and add it to the total
                        elif category in profit_margins:
                            quantity_input = input("Enter quantity sold: ")
                            if quantity_input.isdigit():
                                quantity = int(quantity_input)
                                day_profit += profit_margins[category] * quantity
                            # The invalids to stop user from inputting whatever they want
                            else:
                                print("Invalid input, please enter a valid number")
                        else:
                            print("Invalid input, please enter a valid number")
                    else:
                        print("Invalid input, please enter a valid number")
                
                # Adding the 'day' totals to the week's final complete total
                total_week_profit += day_profit
            
            # Print total profit for the week
            print(f"Total Profit for the week is: ${total_week_profit:.2f}")
            
                
                # Printing the optional dialogue, depending on if they passed 10k or not
            if total_week_profit >= 10000:
                print("You did good this week")
            else:
                print("We didn't reach our goal for this period. More work is needed.")
        
        # Handle work week calculation
        elif period == 3:
            total_workweek_profit = 0
            workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            # Printing the 'For _____' that is seen in the text output 
            for day in workdays:
                print(f"For {day}")
                day_profit = 0
                # Entering the product number, making sure it is a digit and assigning it to the category variable
                while True:
                    category_input = input("Enter product number 1-5 or 0 to stop: ")
                    if category_input.isdigit():
                        category = int(category_input)
                        # Making sure to exit if 0 is inputted
                        if category == 0:
                            break
                      # But if the inputted number IS apart of the main dictionary, test to see if it is a digit, add it to the quantity variable and add it to the total
                        elif category in profit_margins:
                            quantity_input = input("Enter quantity sold: ")
                            if quantity_input.isdigit():
                                quantity = int(quantity_input)
                                day_profit += profit_margins[category] * quantity
                            # The invalids to stop user from inputting whatever they want
                            else:
                                print("Invalid input, please enter a valid number")
                        else:
                            print("Invalid input, please enter a valid number")
                    else:
                        print("Invalid input, please enter a valid number")
                
                total_workweek_profit += day_profit
            
            # Print total profit for the work week
            print(f"Total Profit for the week (business days) is: ${total_workweek_profit:.2f}")
                
                # Printing the optional dialogue, depending on if they passed 10k or not
            if total_workweek_profit >= 10000:
                print("You did good this week (business days)")
            else:
                print("We didn’t reach our goal for this period. More work is needed.")
        
        # Handle weekend calculation
        elif period == 4:
            total_weekend_profit = 0
            weekends = ['Saturday', 'Sunday']
            # Printing the 'For _____' that is seen in the text output 
            for day in weekends:
                print(f"For {day}")
                day_profit = 0
                # Entering the product number, making sure it is a digit and assigning it to the category variable
                while True:
                    category_input = input("Enter product number 1-5 or 0 to stop: ")
                    if category_input.isdigit():
                        category = int(category_input)
                              # Making sure to exit if 0 is inputted
                        if category == 0:
                            break
                     # But if the inputted number IS apart of the main dictionary, test to see if it is a digit, add it to the quantity variable and add it to the total
                        elif category in profit_margins:
                            quantity_input = input("Enter quantity sold: ")
                            if quantity_input.isdigit():
                                quantity = int(quantity_input)
                                day_profit += profit_margins[category] * quantity
                                # The invalids to stop user from inputting whatever they want
                            else:
                                print("Invalid input, please enter a valid number")
                        else:
                            print("Invalid input, please enter a valid number")
                    else:
                        print("Invalid input, please enter a valid number")
                # Print total profit for the weekend which is adding the profit of the two days together
                total_weekend_profit += day_profit
            
            # Print total profit for the weekend
            print(f"Total Profit for the weekend is: ${total_weekend_profit:.2f}")
                
                # Printing the optional dialogue, depending on if they passed 10k or not
            if total_weekend_profit >= 10000:
                print("You did good this weekend")
            else:
                print("We didn’t reach our goal for this period. More work is needed.")
        
        # Handle invalid time period input
        else:
            print("Invalid input, please enter a valid input")
        # The loop that restarts the entire sequence
        print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
        print("Enter:")
        print("1 - For specific Day")
        print("2 - For the Week")
        print("3 - For Week Business Days")
        print("4 - For Weekend days")
        print("0 - Exit")
    else:
        print("Invalid input, please enter a valid input")
