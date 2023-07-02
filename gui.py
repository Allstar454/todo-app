import functions as fun
import PySimpleGUI as sg
import time

label_time = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="time_label")

label_mylist = sg.Text("My To-Do List", text_color="black")

label_blank = sg.Text("")

#Add
label_add = sg.Text("Type in a To-Do to Add or Edit", text_color="black")

inputbox_add = sg.InputText(tooltip="Enter to do", key="add_key")
button_add = sg.Button("Add")

#Edit
listbox_edit = sg.Listbox(values=fun.get_todos(), key="edit_key",
                          enable_events=True, size=(45, 10))
button_edit = sg.Button("Edit")
button_complete = sg.Button('Complete\nor\nRemove', size=(12, 3), key="Complete")
button_exit = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label_time], [label_mylist],
                   [listbox_edit, button_complete], [label_blank],
                   [label_add], [inputbox_add, button_add, button_edit],
                   [button_exit]],
                   font=("Helvetica", 12))

while True:
    action, input_data = window.read() #timeout=1000
    window["time_label"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            else:
                sg.popup('Please type in a To-Do to add. \nSpaces or Blanks are not allowed', title="WARNING", font=("Helvetica", 12))


        case "Edit":
            todos_list = fun.get_todos()

            if input_data["edit_key"]:
                todo_to_edit = input_data["edit_key"][0]
                index_of_edit = todos_list.index(todo_to_edit)
                new_todo = input_data["add_key"].strip()
                if new_todo:
                    todos_list[index_of_edit] = new_todo + '\n'
                    fun.write_todos("w", todos_list)
                    window["edit_key"].update(values=todos_list)
                    window["add_key"].update(value="")
                else:
                    sg.popup('Please type in a To-Do to edit. \nSpaces or Blanks are not allowed', title="WARNING",
                             font=("Helvetica", 12))
            else:
                sg.popup("Please select a To-Do to edit/replace", title="WARNING", font=("Helvetica", 12))


        case "Complete":
            todos_list = fun.get_todos()
            if input_data["edit_key"]:
                completed_todo = input_data["edit_key"][0]
                todos_list.remove(completed_todo)
                fun.write_todos("w", todos_list)
                window["edit_key"].update(values=todos_list)
                window["add_key"].update(value="")
            else:
                sg.popup("Please select a To-Do to complete/remove", title="WARNING", font=("Helvetica", 12))

        case "Exit":
            break

        #case "edit_key":
           # window["add_key"].update(value=input_data['edit_key'][0].strip())

        case sg.WIN_CLOSED:
            break

window.close()
