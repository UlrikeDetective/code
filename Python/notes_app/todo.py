import os

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()  # Normalize input to lowercase
    # Ensure the file exists before reading
    if not os.path.exists('todos.txt'):
        with open('todos.txt', 'w') as file:
            pass
    # Read todos at the start of each loop
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            with open('todos.txt', 'w') as file:
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
                    with open('todos.txt', 'w') as file:
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
                    with open('todos.txt', 'w') as file:
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