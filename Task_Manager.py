tasks = []

def add_task(task):
    tasks.append(task)
    print(f'\nTask {task} has been added')


def completed_task(task):
        if task in tasks:
            tasks.remove(task)
            print(f'\nTask {task} has been marked as completed')
        else:
            print(f"\nTask {task}'s not found. Please retry.")


def show_task(task):
    saat_ini = None
    print(f'\nTasks : ')
    for task in tasks:
        print(f' - {task}')

while True:
    print("\nHere's a few command to choose : \n1) Add Task \n2) Mark Completed Task \n3) Show Tasks \n4) Quit")
    choice = input("Please choose either of the command : ")

    if choice == "1":
        task = input("Enter the task : ")
        add_task(task)

    elif choice == "2":
        task = input("Enter the task to be marked as completed : ")
        completed_task(task)

    elif choice == "3":
        show_task(tasks)

    elif choice == "4":
        print("Goodbye!!")
        break

    else:
        print("\nInvalid Command. Please choose a valid command.")
