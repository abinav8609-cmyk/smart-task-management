tasks = []

while True:
    print("=== Smart Task Management System ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added:", task)

    elif choice == "2":
        if len(tasks) == 0:
            print("no task available")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if len(tasks) == 0:
            print("no tasks to complete")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            task_num = int(input("Enter task number to mark complete: "))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)  # List la irundhu remove pannidum
                print(f"Task '{completed_task}' marked complete!")
            else:
                print("Invalid task number")

    elif choice == "4":
        print("Good bye")
        break

    else:
        print("Invalid choice")