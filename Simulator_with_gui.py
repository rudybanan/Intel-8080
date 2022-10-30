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

sg.theme('DarkBrown6')


def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def MOV(a, b):
    temp = int(registers[b], 16)
    if temp > 255:
        registers[a] = hex(255)
    else:
        registers[a] = registers[b]


def XCHG(x, y):
    registers[x], registers[y] = registers[y], registers[x]


def NOT(x):
    temp = int(registers[x], 16)
    registers[x] = hex(255 - temp)


def INC(x):
    temp = int(registers[x], 16)
    temp += 1
    if temp > 255:
        registers[x] = hex(255)
    else:
        registers[x] = hex(temp)


def DEC(x):
    temp = int(registers[x], 16)
    temp -= 1
    if temp < 0:
        registers[x] = hex(0)
    else:
        registers[x] = hex(temp)


def AND(x, y):
    registers[x] = hex(int(registers[x], 16) & int(registers[y], 16))


def OR(x, y):
    registers[x] = hex(int(registers[x], 16) | int(registers[y], 16))


def XOR(x, y):
    registers[x] = hex(int(registers[x], 16) ^ int(registers[y], 16))


def ADD(x, y):
    temp = int(registers[x], 16) + int(registers[y], 16)
    if temp > 255:
        registers[x] = hex(255)
    else:
        registers[x] = hex(temp)


def SUB(x, y):
    temp = int(registers[x], 16) - int(registers[y], 16)
    if temp < 0:
        registers[x] = hex(0)
    else:
        registers[x] = hex(temp)


def instruction_layout():
    window["_SUBMIT_"].Update(visible=False)
    window["_INITIAL_TEXT_"].Update(visible=False)
    window["_INSTRUCTION_TEXT_"].Update(visible=True)
    window["_INPUT_ERROR_"].Update(visible=False)
    window["_INPUTS_"].Update(visible=False)
    window["_REGISTER_VALUES_"].Update(visible=True)
    window["_INSTRUCTIONS_"].Update(visible=True)
    window["_REGISTER_CHOICE_NAME_"].Update(visible=True)
    window["_REGISTER_CHOICE_"].Update(visible=True)


def input_layout():
    window["_SUBMIT_"].Update(visible=True)
    window["_INITIAL_TEXT_"].Update(visible=True)
    window["_INSTRUCTION_TEXT_"].Update(visible=False)
    window["_INPUTS_"].Update(visible=True)
    window["_REGISTER_VALUES_"].Update(visible=False)
    window["_INSTRUCTIONS_"].Update(visible=False)


def format_values():
    for x in registers:
        registers[x] = hex(int(registers[x], 16))


def update_shown_values():
    window["_AL_VALUE_"].Update(registers["AL"])
    window["_AH_VALUE_"].Update(registers["AH"])
    window["_BL_VALUE_"].Update(registers["BL"])
    window["_BH_VALUE_"].Update(registers["BH"])
    window["_CL_VALUE_"].Update(registers["CL"])
    window["_CH_VALUE_"].Update(registers["CH"])
    window["_DL_VALUE_"].Update(registers["DL"])
    window["_DH_VALUE_"].Update(registers["DH"])


register_choice = [[sg.Combo([x for x in registers.keys()], key="_FIRST_LIST_")],
                   [sg.Combo([x for x in registers.keys()], key="_SECOND_LIST_")]]

register_choice_name = [[sg.Text("First register:")],
                        [sg.Text("Second register:")]]

register_names = [
    [sg.Text("AL register:", key="_AL_TEXT_")],
    [sg.Text("AH register:", key="_AH_TEXT_")],
    [sg.Text("BL register:", key="_BL_TEXT_")],
    [sg.Text("BH register:", key="_BH_TEXT_")],
    [sg.Text("CL register:", key="_CL_TEXT_")],
    [sg.Text("CH register:", key="_CH_TEXT_")],
    [sg.Text("DL register:", key="_DL_TEXT_")],
    [sg.Text("DH register:", key="_DH_TEXT_")],
]
register_values = [
    [sg.Text(registers["AL"], key="_AL_VALUE_")],
    [sg.Text(registers["AH"], key="_AH_VALUE_")],
    [sg.Text(registers["BL"], key="_BL_VALUE_")],
    [sg.Text(registers["BH"], key="_BH_VALUE_")],
    [sg.Text(registers["CL"], key="_CL_VALUE_")],
    [sg.Text(registers["CH"], key="_CH_VALUE_")],
    [sg.Text(registers["DL"], key="_DL_VALUE_")],
    [sg.Text(registers["DH"], key="_DH_VALUE_")],
]
inputs = [
    [sg.InputText(size=(5, 2), key='AL')],
    [sg.InputText(size=(5, 2), key='AH')],
    [sg.InputText(size=(5, 2), key="BL")],
    [sg.InputText(size=(5, 2), key="BH")],
    [sg.InputText(size=(5, 2), key="CL")],
    [sg.InputText(size=(5, 2), key="CH")],
    [sg.InputText(size=(5, 2), key="DL")],
    [sg.InputText(size=(5, 2), key="DH")],
]

instructions = [
    [sg.Button('MOV', size=(5, 2)), sg.Button('XCHG', size=(5, 2))],
    [sg.Button('INC', size=(5, 2)), sg.Button('DEC', size=(5, 2))],
    [sg.Button('NOT', size=(5, 2)), sg.Button('AND', size=(5, 2))],
    [sg.Button('OR', size=(5, 2)), sg.Button('XOR', size=(5, 2))],
    [sg.Button('ADD', size=(5, 2)), sg.Button('SUB', size=(5, 2))],
]

layout = [
    [sg.Text("Enter initial state of Intel 8086 registers in hexadecimal values:", key="_INITIAL_TEXT_"),
     sg.Text("Choose instruction and registers for simulation for simulation:", key="_INSTRUCTION_TEXT_",
             visible=False)],
    [sg.Column(register_choice_name, key="_REGISTER_CHOICE_NAME_", visible=False),
     sg.Column(register_choice, key="_REGISTER_CHOICE_", visible=False)],
    [sg.Column(register_names, key="_REGISTER_NAMES_"), sg.Column(inputs, key="_INPUTS_", visible=True),
     sg.Column(register_values, key="_REGISTER_VALUES_", visible=False),
     sg.Column(instructions, key="_INSTRUCTIONS_", visible=False)],
    [[sg.Button('Submit', key='_SUBMIT_')]],
    [sg.Text("Inputs not hexadecimal or not 8 bit!", key="_INPUT_ERROR_", visible=False)],
]

inputs_given = False

window = sg.Window(title="Simulator of Intel 8086", layout=layout, scaling=2.5, element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if "_SUBMIT_" and not inputs_given:
        for x in registers:
            registers[x] = values[x]
        if inputs_hex_and_8_bit():
            format_values()
            update_shown_values()
            instruction_layout()
            inputs_given = True
        else:
            window["_INPUT_ERROR_"].Update(visible=True)
    if event == "MOV":
        MOV(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    if event == "XCHG":
        XCHG(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    if event == "NOT":
        NOT(values["_FIRST_LIST_"])
    if event == "INC":
        INC(values["_FIRST_LIST_"])
    if event == "DEC":
        DEC(values["_FIRST_LIST_"])
    if event == "AND":
        AND(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    if event == "OR":
        OR(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    if event == "XOR":
        XOR(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    if event == "ADD":
        ADD(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    if event == "SUB":
        SUB(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
    update_shown_values()
window.close()
