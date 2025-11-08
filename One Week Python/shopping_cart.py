print("WELCOME TO OUR STORE!")
print("*********************")

item = input("What item are you purchasing: ")
price = float(input(f"What is the price of {item}: "))
quantity = float(input(f"How many {item} are you buying: "))

print(f"Added {quantity} {item}(s) to the shopping cart!")
print(f"Subtotal: ${price * quantity}")