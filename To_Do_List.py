tasks = []

def add_task():
    task = input("Enter the task to add to the list: ")
    tasks.append(task)
    print(f"{task} is added to your to-do list")

def rem_task():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"The task '{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number! Try again...")

def list_task():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

print("TO DO LIST")

while True:
    choices = """
    A. Add a Task
    B. Remove a Task
    C. View Tasks
    Q. Quit
    """
    print(choices)
    user_choice = input("Enter Your Choice: ").upper()

    if user_choice == 'A':
        add_task()
    elif user_choice == 'B':
        rem_task()
    elif user_choice == 'C':
        list_task()
    elif user_choice == 'Q':
        print("Goodbye!")
        break
    else:
        print("INVALID INPUT")
