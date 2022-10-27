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


inputs = [
    [sg.Text("Enter initial state of Intel 8086 registers in hexadecimal values:", key="_INITIAL_TEXT_")],
    [sg.Text("AL register:", key="_AL_TEXT_"), sg.Push(), sg.InputText(key='AL')],
    [sg.Text("AH register:", key="_AH_TEXT_"), sg.Push(), sg.InputText(key='AH')],
    [sg.Text("BL register:", key="_BL_TEXT_"), sg.Push(), sg.InputText(key="BL")],
    [sg.Text("BH register:", key="_BH_TEXT_"), sg.Push(), sg.InputText(key="BH")],
    [sg.Text("CL register:", key="_CL_TEXT_"), sg.Push(), sg.InputText(key="CL")],
    [sg.Text("CH register:", key="_CH_TEXT_"), sg.Push(), sg.InputText(key="CH")],
    [sg.Text("DL register:", key="_DL_TEXT_"), sg.Push(), sg.InputText(key="DL")],
    [sg.Text("DH register:", key="_DH_TEXT_"), sg.Push(), sg.InputText(key="DH")],
    [sg.Button('Submit', key="_SUBMIT_"),
     sg.Text("Inputs not hexadecimal or not 8 bit!", key="_INPUT_ERROR_", visible=False)],
]
register_values = [
    [sg.Text("AL = ")],
    [sg.Text("AH = ")],
    [sg.Text("BL = ")],
    [sg.Text("BH = ")],
    [sg.Text("CL = ")],
    [sg.Text("CH = ")],
    [sg.Text("DL = ")],
    [sg.Text("DH = ")],
]
instructions = [
    [sg.Button('MOV', key='MOV'), sg.Button('XCHG', key='XCHG')],
    [sg.Button('INC', key='INC'), sg.Button('DEC', key='DEC')],
    [sg.Button('NOT', key='NOT'), sg.Button('AND', key='AND')],
    [sg.Button('OR', key='OR'), sg.Button('XOR', key='XOR')],
    [sg.Button('ADD', key='ADD'), sg.Button('SUB', key='SUB')],
]

layout = [
    [sg.Column(register_values),
     sg.Column(inputs, key="_INPUTS_", visible=True),
     sg.Column(instructions, key="_INSTRUCTIONS_", visible=False)
     ]
]

window = sg.Window(title="Simulator of Intel 8086", layout=layout, size=(550, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if '_Submit_':
        for x in registers:
            registers[x] = values[x.upper()]
        if inputs_hex_and_8_bit():
            window["_INPUT_ERROR_"].Update(visible=False)
            window["_INPUTS_"].Update(visible=False)
            window["_INSTRUCTIONS_"].Update(visible=True)
        else:
            window["_INPUT_ERROR_"].Update(visible=True)
window.close()
