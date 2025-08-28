import json

To_Do_list = []

def Save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(To_Do_list, f)

def Load_tasks():
    global To_Do_list
    try:
        with open("tasks.json", "r") as f:
            To_Do_list = json.load(f)
    except FileNotFoundError:
        To_Do_list = []

def Show_menu():
    print("\n To-Do List 📋")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete some tasks")
    print("4. Quit")

def Show_tasks():
    if not To_Do_list:
        print("Ooh Gosh...The list is empty!!!")
    else:
        for i, task in enumerate(To_Do_list, 1):
            print(f"{i}. {task}")

def Add_task():
    task = input("Enter the task title: ")
    To_Do_list.append(task)
    print("Added task ✅ ")

def Remove_task():
    Show_tasks()
    try:
        index = int(input("The task number you want to delete :"))
        Removed = To_Do_list.pop(index - 1)
        print(f" '{Removed}' deleted ❌ ")
    except (ValueError, IndexError):
        print("Sorry... Invalid number")

# Run the program
Load_tasks()
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
        