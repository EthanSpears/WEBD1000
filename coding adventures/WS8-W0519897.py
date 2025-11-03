temperatures = [14, 16, 18, 17, 20, 19, 15]

# Allow user to add more temperatures
while True:
    entry = input("Enter a new temperature (or type 'done' to finish): ")
    if entry.lower() == "done":
        break
    try:
        temp = float(entry)
        temperatures.append(temp)
    except ValueError:
        print("❌ Please enter a valid number or 'done'.")

# Calculate average
total = sum(temperatures)
avg = total / len(temperatures)

# Find highest and lowest
highest = max(temperatures)
lowest = min(temperatures)

# Count days above 18°C
above_18 = sum(1 for t in temperatures if t > 18)

# Remove duplicates using a set
unique_temps = set(temperatures)

# Print results
print("\n📊 Weekly Temperature Summary")
print("Average temperature:", round(avg, 2))
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Days above 18°C:", above_18)
print("Unique temperature readings:", unique_temps)


input("Press Enter to continue")


books = {
    "Python Basics": 3,
    "Web Design 101": 2,
    "Networking Made Easy": 1
}

while True:
    print("\n--- Library Menu ---")
    for title, qty in books.items():
        print(f"{title:25} copies: {qty}")
    
    action = input("\nEnter 'checkout', 'return', 'summary', or 'exit': ").lower()

    if action == "exit" or "EXIT":
        print("Goodbye! 👋")
        break

    elif action == "checkout":
        book = input("Which book would you like to check out? ")
        if book in books:
            if books[book] > 0:
                books[book] -= 1
                print(f"✅ Checked out one copy of '{book}'.")
            else:
                print(f"❌ Sorry, no copies of '{book}' are available.")
        else:
            print("❌ Book not found in catalog.")

    elif action == "return":
        book = input("Which book are you returning? ")
        if book in books:
            books[book] += 1
            print(f"📥 Returned one copy of '{book}'.")
        else:
            print("❌ Book not found in catalog.")

    elif action == "summary":
        total = sum(books.values())
        fewest_title = min(books, key=books.get)
        print("\n📊 Library Summary")
        print(f"Total books in circulation: {total}")
        print(f"Book with fewest copies: '{fewest_title}' ({books[fewest_title]} copies left)")
    else:
        print("❌ Invalid option. Please choose again.")


input("Press Enter to continue")


items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]

while True:
    print("\n--- Café Sales Menu ---")
    print("1. View Sales Report")
    print("2. Add New Item")
    print("3. Summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n📊 Sales Report")
        print(f"{'Item':15} {'Sales':>5}")
        print("-" * 22)
        for item, qty in zip(items, sales):
            print(f"{item:15} {qty:>5}")

    elif choice == "2":
        new_item = input("Enter new item name: ")
        try:
            qty = int(input(f"Enter sales for {new_item}: "))
            items.append(new_item)
            sales.append(qty)
            print(f"✅ Added {new_item} with {qty} sales.")
        except ValueError:
            print("❌ Please enter a valid number for sales.")

    elif choice == "3":
        total_sales = sum(sales)
        avg_sales = total_sales / len(sales)
        best_index = sales.index(max(sales))
        best_item = items[best_index]

        print("\n📈 Sales Summary")
        print(f"Total sales: {total_sales}")
        print(f"Average sales per item: {round(avg_sales, 2)}")
        print(f"Best-selling item: {best_item} ({sales[best_index]} sales)")

        unique_items = set(items)
        print(f"Unique menu items sold: {unique_items}")

    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice, please try again.")
        

input("Press Enter to continue")


adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2
}

species_seen = set(adoptions.keys())

while True:
    print("\n--- Animal Adoption Center ---")
    for species, count in adoptions.items():
        print(f"{species:10} adopted: {count}")
    entry = input("\nEnter an animal type to log an adoption (or type 'done' to finish): ")
    if entry.lower() == "done":
        break
    species = entry.capitalize()
    species_seen.add(species)
    try:
        num = int(input(f"How many {species} were adopted? "))
        if num < 0:
            print("❌ Cannot log negative adoptions.")
            continue
        adoptions[species] = adoptions.get(species, 0) + num
        print(f"✅ Logged {num} {species} adoption(s).")
    except ValueError:
        print("❌ Please enter a valid number.")
print("\n📊 Adoption Report")
total = sum(adoptions.values())
most_popular = max(adoptions, key=adoptions.get)

for species, count in adoptions.items():
    print(f"{species:10} adopted: {count}")
print(f"\nTotal adoptions: {total}")
print(f"Most popular pet: {most_popular} ({adoptions[most_popular]} adoptions)")
print(f"Unique species seen: {species_seen}")