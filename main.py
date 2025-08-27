# todo.py

todo_list = []

def show_menu():
    print("\n To-Do List 📋")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete some tasks")
    print("4. Quit")

def show_tasks():
    if not todo_list:
        print("Ooh...The list is empty!!!")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task title: ")
    todo_list.append(task)
    print("Added task ✅ ")

def remove_task():
    show_tasks()
    try:
        index = int(input("The task number you want to delete :"))
        removed = todo_list.pop(index - 1)
        print(f" '{removed}' deleted ❌ ")
    except (ValueError, IndexError):
        print("Sorry... Invalid number")

while True:
    show_menu()
    choice = input("your choice:")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Quit")
        break
    else:
        print("Sorry... Invalid option")
        