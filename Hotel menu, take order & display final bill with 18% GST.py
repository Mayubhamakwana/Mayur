# Program 8
menu = {
    1: {"item": "Burger", "price": 100},
    2: {"item": "Pizza", "price": 250},
    3: {"item": "Pasta", "price": 150},
    4: {"item": "Sandwich", "price": 120},
    5: {"item": "Coke", "price": 50}
}

print("Welcome to our Hotel")
print("Menu:")
for key, val in menu.items():
    print(f"{key}. {val['item']} - ₹{val['price']}")

order = []
total = 0
while True:
    choice = int(input("Enter item number to order (0 to finish): "))
    if choice == 0:
        break
    if choice in menu:
        qty = int(input("Enter quantity: "))
        total += menu[choice]["price"] * qty
    else:
        print("Invalid choice!")

gst = total * 0.18
final_bill = total + gst
print(f"Total: ₹{total}")
print(f"GST @18%: ₹{gst}")
print(f"Final Bill: ₹{final_bill}")
