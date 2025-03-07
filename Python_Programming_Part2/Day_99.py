"""
Task  Management  System
"""
def task():
    tasks=[]
    print("________Welcome to Task Management System_________")
    total_task=int(input("Enter how many tasks you want to add="))
    for i in range(1,total_task+1):
        task_name=input(f"Enter the task {i}=")
        tasks.append(task_name)
    print(f"Todays tasks are\n{tasks}")

    while True:
            try:
                operation=int(input("1.Add\n2.Update\n3.Delete\n4.View\n5.Exit\nEnter the Number:"))

                if operation==1:
                    add=input("Enter task you want to add=")
                    tasks.append(add)
                    print(f"Task {add} has been Successfully added.")

                elif operation==2:
                    update_task=input("Enter the task name you want to update=")
                    if update_task in tasks:
                        new=input("Enter the New task=")
                        ind=tasks.index(update_task)
                        tasks[ind]=new
                        print(f"Updated task '{update_task}' to '{new}'")

                    else:
                        print("Task not found.")

                elif operation==3:
                    del_task=input("Which task you want to delete=")
                    if del_task in tasks:
                        ind=tasks.index(del_task)
                        del tasks[ind]
                        print(f"Task '{del_task}' has been deleted..")

                    else:
                        print("Task not found..")

                elif operation==4:
                    print(f"Total tasks={tasks}")

                elif operation==5:
                    print("Closing the Program..")
                    break

                else:
                    print("Invalid Input")

            except ValueError:
                print("Invalid Input. Please Enter a valid number.")

if __name__=="__main__":
    task()




