#Parker Behagg
#5/13/2026
#a simple task tracking program

def main():
    user_input = ''
    tasks = [{"name":"placeholder", "priority":'1', "status":False}, {"name":"placeholder2", "priority":'2', "status":True}] #placeholders for development purposes
    exit=False
    welcome()
    while not exit:
        user_input = displayMenu(user_input)
        if user_input == "1":
            print("selected option: 1. add task")
            add_task(tasks)
        elif user_input == "2":
            print("selected option: 2. view tasks")
            view_tasks(tasks)
        elif user_input == "3":
            print("selected option: 3. complete task")
            complete_task(tasks)
        elif user_input == "4":
            print("selected option: 4. delete task")
        elif user_input == "5":
            print("selected option: 5. exit")
            exit=True

def displayMenu(user_input):
    print()
    print("------------------menu----------------")
    print("1. add task")
    print("2. view tasks")
    print("3. complete task")
    print("4. delete task")
    print("5. exit")
    print("--------------------------------------")
    user_input = input("selection number: ")
    while user_input.lower() not in [
    "1",
    "2",
    "3",
    '4',
    '5', 
    ]:
        user_input = input("invalid entry, please re-enter a selection number: ")


    return user_input

def welcome():
    print("welcome to taskker, the task tracking program")
    print()

def add_task(tasks):
    task_name = ""
    task_priority = ""
    task_status = False
    task_value = {}
    print()
    task_name = input("please enter the name of the task: ")
    task_priority = input("please enter the task's prority on a scale of 1-3: ")
    while task_priority not in ["1", "2", "3"]:
        task_priority = input("inalid input, please re-enter the task's prority on a scale of 1-3: ")
    task_value = {"name":task_name, "priority":task_priority, "status":task_status}
    tasks.append(task_value)
    return tasks
        
def view_tasks(tasks):
    print()
    print("-------tasks-list-------")
    for i in range(0, len(tasks)):
        taask_val = tasks[i]
        name = taask_val["name"]
        priority = taask_val["priority"]
        status = taask_val["status"]
        _orX = ""
        if status:
            _orX = "X"
        else:
            _orX = "_"
        print(f"[{_orX}]{i+1}. {name} | Prioity: {priority}")

def filter_tasks(tasks):
    filtered = []
    for i in range(0, len(tasks)):
        task_val = tasks[i]        
        status = task_val["status"]
        if not status:
            filtered.append(tasks[i])
    return filtered


def complete_task(tasks):
    print()
    print("please select a task to complete")
    filtered_tasks = filter_tasks(tasks)
    print("------------------------")
    for i in range(len(filtered_tasks)):
        taask_val = filtered_tasks[i]
        name = taask_val["name"]
        priority = taask_val["priority"]
        status = taask_val["status"]
        _orX = ""
        if status:
            _orX = "X"
        else:
            _orX = "_"
        print(f"[{_orX}]{i+1}. {name} | Prioity: {priority}")

main()