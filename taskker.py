#Parker Behagg
#5/13/2026
#a simple task tracking program

import json

def main():
    user_input = ''
    tasks = []
    exit=False
    welcome()
    tasks = load_save(tasks)
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
            delete_task(tasks)
        elif user_input == "5":
            print("selected option: 5. exit")
            save(tasks)
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


def complete_task(tasks):
    print()
    from_user = 0
    print("please select a task to complete")
    print("------------------------")
    for i in range(len(tasks)):
        task_val = tasks[i]
        name = task_val["name"]
        priority = task_val["priority"]
        status = task_val["status"]
        _orX = ""
        if status:
            _orX = "X"
        else:
            _orX = "_"
        print(f"[{_orX}]{i+1}. {name} | Priority: {priority}")
    print("------------------------")
    from_user = int(input("selection: "))
    while not (0 < from_user <= len(tasks)):
        from_user = int(input("invalid selection, please enter a valid task number: "))
    from_user = from_user - 1
    task_dict = tasks[from_user]
    task_dict["status"] = True
    tasks[from_user] = task_dict        


def delete_task(tasks):
    print()
    from_user = 0
    print("please select a task to delete")
    print("------------------------")
    for i in range(len(tasks)):
        task_val = tasks[i]
        name = task_val["name"]
        priority = task_val["priority"]
        status = task_val["status"]
        _orX = ""
        if status:
            _orX = "X"
        else:
            _orX = "_"
        print(f"[{_orX}]{i+1}. {name} | Priority: {priority}")
    print("------------------------")
    try:
        from_user = int(input("selection: "))
    except:
        from_user = int(input("invalid selection, please enter a valid task number: "))
    while not (0 < from_user <= len(tasks)):
        try:
            from_user = int(input("invalid selection, please enter a valid task number: "))
        except:
            from_user = int(input("invalid selection, please enter a valid task number: "))
    from_user = from_user - 1
    tasks.pop(from_user) 


def load_saved_tasks():
    try:
        with open("taskker_saved_tasks.json", "r", encoding="utf-8") as f:
            temp_tasks = json.load(f)
        return temp_tasks
    except:
        print("no saves availible, please select option 3.")

def save(tasks):
    data=tasks
    with open("taskker_saved_tasks.json", "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_save(tasks):
    load = False
    while not load:
        temp_tasks=load_saved_tasks()
        print("---------load--------")
        print("1. load saved tasks")
        print("2. list saved tasks")
        print("3. clear saved tasks")
        print("---------------------")
        selection=input("selection: ")
        while selection not in ["1", "2", "3"]:
            print()
            selection=input("invalid selection, please re-enter the selection number: ")
            print()
        while selection == "2":
            if selection == "2":
                view_tasks(temp_tasks)
                print()
                selection = input("would you like to load these saved tasks? (y/n): ")
                while selection not in ["n", "y"]:
                    selection = input("invalid selection, please enter 'y' or 'n': ")
                if selection == "y":
                    tasks=temp_tasks
                    load=True
                elif selection == "n":
                    load = False
        if selection == "1":
            tasks=temp_tasks
            load=True
        elif selection == "3":
            tasks=[]
            load=True
    return tasks
main()