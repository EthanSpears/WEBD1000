# Travel record stored as a tuple
ticket = ("Halifax", "Toronto", "AC702", 349.99)

# Unpack the tuple into variables
origin, destination, flight_no, price = ticket

# Print the details
print("✈️ Travel Record")
print(f"From {origin} to {destination} on flight {flight_no}")
print(f"Ticket Price: ${price}")

# Personalized message with emoji flair
print(f"\n🧳 Get ready! You're flying from {origin} 🌎 to {destination} ✈️ on {flight_no} for just ${price}!")


input("Press Enter to continue")


tickets = [
    ("Halifax", "Toronto", "AC702", 349.99),
    ("Halifax", "Vancouver", "WS305", 599.50),
    ("Halifax", "New York", "DL120", 429.00),
    ("Halifax", "London", "BA208", 899.75),
]

# Print all possible outcomes
for origin, destination, flight_no, price in tickets:
    print("✈️ Travel Record")
    print(f"From {origin} to {destination} on flight {flight_no}")
    print(f"Ticket Price: ${price}")
    print(f"🧳 Pack your bags! You're flying from {origin} 🌎 to {destination} ✈️ on {flight_no} for ${price}!\n")
    
    
    input("Press Enter to continue")
    
    
 # Function to update a flight record
def update_flight(f, new_dest, new_price):
    # f is a tuple: (origin, destination, price)
    return (f[0], new_dest, new_price)

# Initial flight record
flight = ("Halifax", "Toronto", 349.99)
print("Starting flight:", flight)

# Interactive loop
while True:
    choice = input("\nDo you want to update this flight? (yes/no): ").lower()
    if choice == "no":
        break
    elif choice == "yes":
        new_dest = input("Enter new destination: ")
        try:
            new_price = float(input("Enter new price: "))
            flight = update_flight(flight, new_dest, new_price)
            print("✅ Updated flight:", flight)
        except ValueError:
            print("❌ Please enter a valid number for price.")
    else:
        print("❌ Invalid choice. Please type 'yes' or 'no'.")

print("\nFinal flight record:", flight)   


input("Press Enter to continue")


orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]


print("📋 Pizza Order Summaries")
for name, size, toppings in orders:
    toppings_str = " & ".join(toppings)
    print(f"{name} ordered a {size} pizza with {toppings_str}.")


large_count = sum(1 for _, size, _ in orders if size == "Large")
print(f"\n🍕 Number of Large pizzas ordered: {large_count}")


unique_toppings = set()
for _, _, toppings in orders:
    unique_toppings.update(toppings)

print(f"🧀 Unique toppings ordered: {unique_toppings}")