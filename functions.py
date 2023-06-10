FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as f:
        todos = f.readlines()
        return todos


def write_todos(write_mode, todo_arg, filepath=FILEPATH):
    with open(filepath, write_mode) as f:
        if write_mode == "a":
            f.write(todo_arg)
        elif write_mode == "w":
            f.writelines(todo_arg)

