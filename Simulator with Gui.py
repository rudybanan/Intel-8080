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


def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def register_state():
    print("\nInitial state of the registers of Intel 8086 processor: \n")
    for register in registers:
        print(register, "=", registers[register])


layout = [
    [sg.Text("Enter initial state of Intel 8086 registers in hexadecimal values:")],
    [sg.Text("AL register:"), sg.Push(), sg.InputText(key='AL')],
    [sg.Text("AH register:"), sg.Push(), sg.InputText(key='AH')],
    [sg.Text("BL register:"), sg.Push(), sg.InputText(key="BL")],
    [sg.Text("BH register:"), sg.Push(), sg.InputText(key="BH")],
    [sg.Text("CL register:"), sg.Push(), sg.InputText(key="CL")],
    [sg.Text("CH register:"), sg.Push(), sg.InputText(key="CH")],
    [sg.Text("DL register:"), sg.Push(), sg.InputText(key="DL")],
    [sg.Text("DH register:"), sg.Push(), sg.InputText(key="DH")],
    [sg.Button('Submit'), sg.Button("Quit")],
    [sg.Text("Inputs not hexadecimal or not 8 bit!", key="_INPUT_ERROR_", visible=False)]
]

window = sg.Window(title="Simulator of Intel 8086", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':  # if user closes window or clicks cancel
        break
    if event == 'Submit':
        for x in registers:
            registers[x] = values[x]
        if inputs_hex_and_8_bit():
            break
        else:
            window["_INPUT_ERROR_"].Update(visible=True)

window.close()
