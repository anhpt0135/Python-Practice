todos = []

while True:
    user_action = input("add, show, edit or exit: ")
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Wrong input, only add, show, exit")

print("Bye!!!")