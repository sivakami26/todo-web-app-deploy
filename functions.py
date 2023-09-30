def get_todos(filepath="todo.txt"):
    """
    Read the file and store its contents in a list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos, filepath="todo.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos)