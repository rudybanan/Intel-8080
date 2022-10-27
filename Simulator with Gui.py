import PySimpleGUI as sg

registers = {"AL": None,
             "AH": None,
             "BL": None,
             "BH": None,
             "CL": None,
             "CH": None,
             "DL": None,
             "DH": None,
             }

sg.theme('DarkAmber')

layout = [
    [sg.Text("Enter initial state of Intel 8086 registers:"), sg.Text("Choose action for program to execute:")],
    [sg.Text("AL register:"), sg.InputText(), sg.Button("MOV")],
    [sg.Text("AH register:"), sg.InputText(), sg.Button("XCHG")],
    [sg.Text("BL register:"), sg.InputText()],
    [sg.Text("BH register:"), sg.InputText()],
    [sg.Text("CL register:"), sg.InputText()],
    [sg.Text("CH register:"), sg.InputText()],
    [sg.Text("DL register:"), sg.InputText()],
    [sg.Text("DH register:"), sg.InputText()],
    [sg.Button('Accept'), sg.Button("Quit")]
]

window = sg.Window(title="Simulator of Intel 8086", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':  # if user closes window or clicks cancel
        break

window.close()
