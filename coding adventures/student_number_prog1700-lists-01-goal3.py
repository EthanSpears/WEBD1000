#goal 3#

inventory = ["milk", "bread", "eggs"]
inventory.append("butter")
inventory.append("cheese")

print(inventory)
inventory.insert(0, "apples")
print(inventory)
index = inventory.index("bread")
inventory[index] = "whole grain bread"
print(inventory)
inventory.remove("eggs")
print(inventory)
print("Items left in inventory:", len(inventory))