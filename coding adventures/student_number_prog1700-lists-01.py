# goal 1 #


Movies = ["how to train your dragon", "cloverfield", "a quiet place", "avengers: age of ultron", "The Batman"]

print(Movies)
Movies[1]= "titanic"
print(Movies)
Movies.remove("a quiet place")
print(Movies)

print(Movies[0])
print(Movies[1])
print(Movies[2])
print(Movies[3])


# goal 2 #

Numbers = [10, 20, 30, 40, 50]

print(Numbers[2])
print(Numbers[3:])
total = 0
for i in range(len(Numbers)):
    total += Numbers[i]
    print("Total:", total)

for i in range(len(Numbers)): 
    print(f"Position {i + 1}: {Numbers[i]}")
    

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


#goal 4#

tasks = []

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f'Task "{task}" added.')

    elif choice == "2":
        if not tasks:
            print("Your task list is empty! Nothing to remove.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f'Task "{removed}" removed.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "3":
        if not tasks:
            print("Your task list is empty.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Thanks for using the to-do list manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")