# Module 5 Lab-5
# Ben Meadmore
# March 5, 2025
# This program calculates and displays store and employee bonus amounts based on monthly sales and sales increase percentages.
# The main function
# This function gets the monthly sales amount from the user
def getSales():
    monthlySales = float(input("Enter the monthly sales amount: "))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input("Enter the percent of sales increase (as a decimal): "))
    return salesIncrease

# This function determines the store bonus amount
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    salesIncrease = salesIncrease / 100  # Convert to decimal form
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount


# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    
    if storeAmount == 6000 and empAmount == 75:
        print("Congrats! You have reached the highest bonus amounts possible!")

# Main function to execute the program
def main():
    # Get input from the user
    monthlySales = getSales()
    salesIncrease = getIncrease()

    # Calculate bonuses
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)

    # Print the results
    printBonus(storeAmount, empAmount)

# Run the program
main()
