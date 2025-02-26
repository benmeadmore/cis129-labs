# cis129_lab03_coffeeShop.py
# Author: [Ben Meadmore]
# Date: [February 26]
# Description: A simple coffee shop program that calculates the total cost of an order with tax.

# Prices of items
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06  # 6% tax

# User input
print("***************************************")
print("My Coffee and Muffin Shop")
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
print("***************************************\n")

# Calculate costs
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)
tax = subtotal * tax_rate
total = subtotal + tax

# Print receipt
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at $5 each: $ {num_coffees * coffee_price:.2f}")
print(f"{num_muffins} Muffins at $4 each: $ {num_muffins * muffin_price:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("***************************************")
