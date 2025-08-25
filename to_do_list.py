tasks = []
def show_task():
    if not tasks:
        print("Hear is no  any task :")
    else:
        print("Hear is the list of task :")
        for i, task in enumerate(tasks, start=1):
            status = "completed" if task['done'] else "due till the now"
            print(f"{i}.{task['title']} [{status}]")
    print()
def add_task():
    title = input("Enter your task : ")
    tasks.append({'title': title, 'done': False})
    print(f"Task '{title}' added\n")

def mark_done():
    show_task()
    try:
        task_num = int(input("Enter the number that you want to make done : "))
        tasks[task_num -1] ['done'] = True
        print("Task marked as done ")
    except(IndexError, ValueError):
        print("Enter valid number\n")
def delete_task():
    show_task()
    try:
        task_num = int(input("Enter the number which task want to delete : "))
        removed = tasks.pop(task_num -1)
        print(f"Task '{removed['title']}' deleted !")
    except(IndexError, ValueError):
        print("Envalid input please check your input :")
while True:
    print(" ----to do list menue----")
    print("1. show task")
    print("2. add task")
    print("3. mark done on task")
    print("4. delete any task"  )
    print("5. exit")
    choice = int(input("Enter the value between 1 - 5 : "))
    if choice == 1:
        show_task()
    elif choice == 2:
        add_task()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("good-bay")
        break
    else:
        print("Invalid choice try again /n")