FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def set_todos(todos, filepath=FILEPATH):
    """
    Write the list of to-do items in file to store it.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)
