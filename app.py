def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append(task)
    print(f"Task '{task}' added!")

def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(task_list, 1):
            print(f"{index}. {task}")

def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        try:
            task_index = int(input("\nEnter the task number to delete: ")) - 1
            if 0 <= task_index < len(task_list):
                removed_task = task_list.pop(task_index)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
