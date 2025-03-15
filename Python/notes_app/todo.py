import os

print("Script started") # Add this line at the beginning

# Define the file path relative to the script location
TODOS_FILE = os.path.join(os.path.dirname(__file__), 'todos.txt')

while True:
    try:
        user_action = input("Type add, show, edit, complete or exit: ").strip().lower()  # Normalize input to lowercase
        
        # Ensure the file exists before reading
        if not os.path.exists(TODOS_FILE):
            with open(TODOS_FILE, 'w') as file:
                pass
                
        # Read todos at the start of each loop
        with open(TODOS_FILE, 'r') as file:
            todos = file.readlines()
        
        match user_action:
            case 'add':
                todo = input("Enter a todo: ") + "\n"
                todos.append(todo)
                with open(TODOS_FILE, 'w') as file:
                    file.writelines(todos)
            case 'show':
                if todos:
                    for index, item in enumerate(todos):
                        item = item.strip('\n')
                        row = f"{index + 1} - {item}"
                        print(row)
                else:
                    print("No todos found.")
            case 'edit':
                try:
                    number = int(input("Number of the todo to edit: ")) - 1
                    if 0 <= number < len(todos):
                        new_todo = input("Enter new todo: ")
                        todos[number] = new_todo + '\n'
                        with open(TODOS_FILE, 'w') as file:
                            file.writelines(todos)
                    else:
                        print("Invalid number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            case 'complete':
                try:
                    number = int(input("Number of the todo to complete: ")) - 1
                    if 0 <= number < len(todos):
                        todo_to_remove = todos.pop(number).strip('\n')
                        with open(TODOS_FILE, 'w') as file:
                            file.writelines(todos)
                        print(f"Todo '{todo_to_remove}' was removed from the list.")
                    else:
                        print("Invalid number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            case 'exit':
                print("Bye!")
                break
            case _:
                print("Invalid action. Please choose add, show, edit, complete, or exit.")
    except Exception as e:
        print(f"An error occurred: {e}")

# in Terminal python3 /Users/ulrike_imac_air/projects/code/Python/notes_app/todo.py