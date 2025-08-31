# todo_list.py

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("\nEnter task title: ")
    tasks.append({"title": title, "done": False})
    print("✅ Task added!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("\nEnter task number to remove: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"🗑 Removed task: {removed['title']}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Please enter a valid number!")

def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("\nEnter task number to mark as done: "))
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]["done"] = True
                print(f"✔ Task marked as done: {tasks[choice - 1]['title']}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Please enter a valid number!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("\n👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
