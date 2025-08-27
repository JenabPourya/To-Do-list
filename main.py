# todo.py

ToDo_list = []

def Show_menu():
    print("\n To-Do List 📋")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete some tasks")
    print("4. Quit")

def Show_tasks():
    if not ToDo_list:
        print("Ooh Gosh...The list is empty!!!")
    else:
        for i, task in enumerate(ToDo_list, 1):
            print(f"{i}. {task}")

def Add_task():
    task = input("Enter the task title: ")
    ToDo_list.append(task)
    print("Added task ✅ ")

def Remove_task():
    Show_tasks()
    try:
        index = int(input("The task number you want to delete :"))
        Removed = ToDo_list.pop(index - 1)
        print(f" '{Removed}' deleted ❌ ")
    except (ValueError, IndexError):
        print("Sorry... Invalid number")

while True:
    Show_menu()
    choice = input("your choice:")
    if choice == "1":
        Show_tasks()
    elif choice == "2":
        Add_task()
    elif choice == "3":
        Remove_task()
    elif choice == "4":
        print("Quit")
        break
    else:
        print("Sorry... Invalid option")
        