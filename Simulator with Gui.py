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


def clearing_layout():
    window["_INITIAL_TEXT_"].Update(visible=False)
    window["_AL_TEXT_"].Update(visible=False)
    window["_AH_TEXT_"].Update(visible=False)
    window["_BL_TEXT_"].Update(visible=False)
    window["_BH_TEXT_"].Update(visible=False)
    window["_CL_TEXT_"].Update(visible=False)
    window["_CH_TEXT_"].Update(visible=False)
    window["_DL_TEXT_"].Update(visible=False)
    window["_DH_TEXT_"].Update(visible=False)
    window['AL'].Update(visible=False)
    window['AH'].Update(visible=False)
    window['BL'].Update(visible=False)
    window['BH'].Update(visible=False)
    window['CL'].Update(visible=False)
    window['CH'].Update(visible=False)
    window['DL'].Update(visible=False)
    window['DH'].Update(visible=False)
    window["_INPUT_ERROR_"].Update(visible=False)


def show_instructions():
    window["MOV"].Update(visible=True)
    window["XCHG"].Update(visible=True)
    window["INC"].Update(visible=True)
    window["DEC"].Update(visible=True)
    window["NOT"].Update(visible=True)
    window["AND"].Update(visible=True)
    window["OR"].Update(visible=True)
    window["XOR"].Update(visible=True)
    window["ADD"].Update(visible=True)
    window["SUB"].Update(visible=True)


layout = [
    [sg.Text("Enter initial state of Intel 8086 registers in hexadecimal values:", key="_INITIAL_TEXT_")],
    [sg.Text("AL register:", key="_AL_TEXT_"), sg.Push(), sg.InputText(key='AL')],
    [sg.Text("AH register:", key="_AH_TEXT_"), sg.Push(), sg.InputText(key='AH')],
    [sg.Text("BL register:", key="_BL_TEXT_"), sg.Push(), sg.InputText(key="BL")],
    [sg.Text("BH register:", key="_BH_TEXT_"), sg.Push(), sg.InputText(key="BH")],
    [sg.Text("CL register:", key="_CL_TEXT_"), sg.Push(), sg.InputText(key="CL")],
    [sg.Text("CH register:", key="_CH_TEXT_"), sg.Push(), sg.InputText(key="CH")],
    [sg.Text("DL register:", key="_DL_TEXT_"), sg.Push(), sg.InputText(key="DL")],
    [sg.Text("DH register:", key="_DH_TEXT_"), sg.Push(), sg.InputText(key="DH")],
    [sg.Button('Submit')],
    [sg.Text("Inputs not hexadecimal or not 8 bit!", key="_INPUT_ERROR_", visible=False)],
    [sg.Button('MOV', key='MOV', visible=False), sg.Push(), sg.Button('XCHG', key='XCHG', visible=False)],
    [sg.Button('INC', key='INC', visible=False), sg.Push(), sg.Button('DEC', key='DEC', visible=False)],
    [sg.Button('NOT', key='NOT', visible=False), sg.Push(), sg.Button('AND', key='AND', visible=False)],
    [sg.Button('OR', key='OR', visible=False), sg.Push(), sg.Button('XOR', key='XOR', visible=False)],
    [sg.Button('ADD', key='ADD', visible=False), sg.Push(), sg.Button('SUB', key='SUB', visible=False)],
]

window = sg.Window(title="Simulator of Intel 8086", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    if event == 'Submit':
        for x in registers:
            registers[x] = values[x]
        if inputs_hex_and_8_bit():
            clearing_layout()
            show_instructions()
        else:
            window["_INPUT_ERROR_"].Update(visible=True)

window.close()
