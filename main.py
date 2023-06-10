from functions import get_todos, write_todos
import time

print("It is", time.strftime("%b %d, %Y %H:%M:%S"))

while True:

    user_action = input("Type : add, show, edit, complete  or exit :  ").lower().strip()

    if user_action.startswith("add "):
        todo = user_action[4:].capitalize() + "\n"
        write_todos("a", todo)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            for index, item in enumerate(file.readlines()):
                print(f"{index + 1} - {item}", end="")

    elif user_action.startswith("edit "):
        try:
            num_edit = int(user_action[5:])
            new_todo = input("Enter new to do : ").capitalize() + "\n"

            todo_list = get_todos()

            todo_list[num_edit - 1] = new_todo

            write_todos("w", todo_list)

        except:
            print("Invalid edit input or Out of range edit no.")

    elif user_action.startswith("complete "):
        try:
            num_comp = int(user_action[9:])

            todo_list = get_todos()

            todo_remove = todo_list[num_comp - 1].strip("\n")

            print(f"Todo > {todo_remove} < was removed form the list")
            todo_list.pop(num_comp - 1)
            write_todos("w", todo_list)

        except:
            print("Invalid complete or Out of range list no.")

    elif user_action.startswith("exit"):
        print("Bye Bye!")
        break

    else:
        print("Command is not valid!")
