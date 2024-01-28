user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for element in todos:
                print(element)
        case "exit":
            break
        case _:
            print("Wrong Type!!!...")

print("Bye!")