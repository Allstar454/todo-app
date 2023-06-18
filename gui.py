import functions
import PySimpleGUI as sg


input_label = sg.Text("Type in a to-do")
input_box1 = sg.InputText(tooltip="Enter to do")
box1_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[input_label], [input_box1, box1_button]])

window.read()
window.close()
