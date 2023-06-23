import functions
import PySimpleGUI as sg


input_label = sg.Text("Type in a to-do")
input_box1 = sg.InputText(tooltip="Enter to do", key="input1")
box1_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[input_label], [input_box1, box1_button]],
                   font=("Helvetica", 15))

while True:
    action, result = window.read()
    print(action)
    print(result)

    match action:
        case "Add":
            todos = functions.get_todos()
            todos.append(result["input1"]+'\n')
            functions.write_todos("w", todos)
        case sg.WIN_CLOSED:
            break

window.close()
