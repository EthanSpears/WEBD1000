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