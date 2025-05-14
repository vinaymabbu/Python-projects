# Load existing items
# 1.create a new item
# 2.list items
# 3.mark item as complete
# 4.save items
import json



file_name="todo_list.json"
def load_tasks():
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}
    

def save_tasks(tasks):
    try:
        with open(file_name,"w") as file:
            return json.dump(tasks,file)
    except:
        print("faied to save")


def view_tasks(tasks):
    task_list=tasks["tasks"]
    if len(tasks["tasks"])==0:
        print("no tasks are available")
    else:
        print("your To-Do list :")
        for idx,task in enumerate(task_list):
            status="[completed]" if task["complete"] else "[pending]"
            print(f"{idx+1}.{task['description']}|{status}")
    
def mark_tasks(tasks):
    try:
        view_tasks(tasks)
        task_number=int(input("enter the number to mark it as complete").strip())
        if 1<=task_number<=len(tasks):
            tasks["tasks"][task_number-1]["complete"]=True
            save_tasks(tasks)
            print("mark as complete")
        else:
            print("invalid task number")
    except:
        print("error marking the task")




def create_task(tasks):
    description=input("enter the task description :").strip()
    if description:
        tasks["tasks"].append({"description":description,"complete":False})
        save_tasks(tasks)
        print("created successfully")
    else:
        print("description cannot be empty")
    

def main():
    
  
    tasks=load_tasks()
    

    while True:
        print("\n To-Do list manager")
        print("1.view task")
        print("2.create task")
        print("3.complete task")
        print("4.exit")

        choice=input("enter your choice : ").strip()

        if choice=="1":
            view_tasks(tasks)
        elif choice=="2":
            create_task(tasks)
        elif choice=="3":
            mark_tasks(tasks)
        elif choice=="4":
            print("bye bye")
        else:
            print("invalid")

main()