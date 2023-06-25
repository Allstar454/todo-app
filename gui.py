import functions as fun
import PySimpleGUI as sg

#Add
label_add = sg.Text("Type in a To-Do")

inputbox_add = sg.InputText(tooltip="Enter to do", key="add_key")
button_add = sg.Button("Add")

#Edit
listbox_edit = sg.Listbox(values=fun.get_todos(), key="edit_key",
                          enable_events=True, size=(45, 10))
button_edit = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label_add], [inputbox_add, button_add],
                   [listbox_edit, button_edit]],
                   font=("Helvetica", 12))

while True:
    action, input_data = window.read()
    print(action)
    print(input_data)

    match action:

        case "Add":
            todos_list = fun.get_todos()
            if input_data["add_key"].strip():
                todos_list.append(input_data["add_key"]+'\n')
                fun.write_todos("w", todos_list)
                window["edit_key"].update(values=todos_list)
                window["add_key"].update(value="")

        case "Edit":
            todos_list = fun.get_todos()
            index_of_edit = ""

            if input_data["edit_key"]:
                todo_to_edit = input_data["edit_key"][0]
                if todo_to_edit:
                    index_of_edit = todos_list.index(todo_to_edit)

            new_todo = input_data["add_key"].strip()

            if new_todo and index_of_edit >= 0:
                todos_list[index_of_edit] = new_todo+'\n'
                fun.write_todos("w", todos_list)
                window["edit_key"].update(values=todos_list)
                window["add_key"].update(value="")

        case "edit_key":
            window["add_key"].update(value=input_data['edit_key'][0].strip())

        case sg.WIN_CLOSED:
            break

window.close()
