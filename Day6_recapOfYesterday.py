todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Type todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.capitalize()}"
                print(row)
        case "edit":
            number = int(input("Input number of todo to edit: "))
            number = number - 1
            new_todo = input("New todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Input number of todo to complete: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break
        case _:
            print("Wrong typing...")


print("Bye!!!")
