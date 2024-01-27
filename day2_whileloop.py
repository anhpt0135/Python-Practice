command_prompt = "Add todo list: "
todos = []
while True:
    todo = input(command_prompt)
    todo = todo.capitalize()
    todos.append(todo)
    print(todos)
    print(type(todos))


