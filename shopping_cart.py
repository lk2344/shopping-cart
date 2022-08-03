# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

selected_products = [] 

import datetime
now = datetime.datetime.now()
#https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

while True:
    selected_id = input("Please input a product id, or 'DONE': " )

    if selected_id.upper() == "DONE":
        break # break out of the while loop 
    else:
        #print("LOOKING UP PRODUCT", selected_id)
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0] # this will trigger an IndexError if there are no matching products
        selected_products.append(matching_product)
        # continue the while loop
        # code snipet from Slack channel to get started


print('--------------------------------')
print('GREEN FOODS GROCERY')
print('WWW.GREEN-FOODS-GROCERY.COM')
print('--------------------------------')
print("CHECKOUT AT:", now.strftime("%Y-%m-%d %H:%M"))
print('--------------------------------')
print('SELECTED PRODUCTS:')

from collections import defaultdict
collect = defaultdict(dict)

for key in selected_products:
    collect[key['name']] = key['price']

x = (dict(collect))
for key, value in x.items():
    print(key,'(', to_usd(value),')') 
# from my miderm challenge 2, question B

values = x.values()
subtotal = sum(values)
# https://tutorial.eyehunts.com/python/python-sum-dictionary-values-by-key-example-code/#:~:text=For%20example%2C%20if%20you%20want,the%20sum%20of%20the%20values.
print('--------------------------------')
print('SUBTOTAL:',to_usd(subtotal))

tax = subtotal * 0.0875
print('TAX:',to_usd(tax))

print('TOTAL:',to_usd(subtotal + tax))

print('--------------------------------')
print('THANKS FOR SHOPPING AT GREEN FOODS GROCERY')
print('SEE YOU AGAIN SOON!')
print('--------------------------------')