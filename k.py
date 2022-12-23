import PySimpleGUI as sg
from random import *

memory = []
for i in range(65536):
    memory.append(randint(0, 255))

registers = {"AL": None,
             "AH": None,
             "BL": None,
             "BH": None,
             "CL": None,
             "CH": None,
             "DL": None,
             "DH": None,
             }

sg.theme('Topanga')


def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def correct_memory(x):
    try:
        return int(x, 16) < 0x10000
    except ValueError:
        return False


#################################################
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


#################################################
def NOT_MEM(x):
    a = int(x, 16)
    temp = memory[a]
    memory[a] = 255 - temp


def INC_MEM(x):
    a = int(x, 16)
    temp = memory[a]
    temp += 1
    if temp > 255:
        memory[a] = 255
    else:
        memory[a] = temp


def DEC_MEM(x):
    a = int(x, 16)
    temp = memory[a]
    temp -= 1
    if temp < 0:
        memory[a] = 0
    else:
        memory[a] = temp


#################################################
def MOV_MEM_REG(x, y):
    a = int(x, 16)
    memory[a] = int(registers[y], 16)


def XCHG_MEM_REG(x, y):
    a = int(x, 16)
    memory[a], registers[y] = int(registers[y], 16), hex(memory[a])


def AND_MEM_REG(x, y):
    a = int(x, 16)
    memory[a] = memory[a] & int(registers[y], 16)


def OR_MEM_REG(x, y):
    a = int(x, 16)
    memory[a] = memory[a] | int(registers[y], 16)


def XOR_MEM_REG(x, y):
    a = int(x, 16)
    memory[a] = memory[a] ^ int(registers[y], 16)


def ADD_MEM_REG(x, y):
    a = int(x, 16)
    temp = memory[a] + int(registers[y], 16)
    if temp > 255:
        memory[a] = 255
    else:
        memory[a] = temp


def SUB_MEM_REG(x, y):
    a = int(x, 16)
    temp = memory[a] - int(registers[y], 16)
    if temp < 0:
        memory[a] = 0
    else:
        memory[a] = temp


#################################################
def MOV_REG_MEM(x, y):
    a = int(y, 16)
    registers[x] = hex(memory[a])


def XCHG_REG_MEM(x, y):
    a = int(y, 16)
    registers[x], memory[a] = hex(memory[a]), int(registers[x], 16)


def AND_REG_MEM(x, y):
    a = int(y, 16)
    registers[x] = hex(int(registers[x], 16) & memory[a])


def OR_REG_MEM(x, y):
    a = int(y, 16)
    registers[x] = hex(int(registers[x], 16) | memory[a])


def XOR_REG_MEM(x, y):
    a = int(y, 16)
    registers[x] = hex(int(registers[x], 16) ^ memory[a])


def ADD_REG_MEM(x, y):
    a = int(y, 16)
    temp = memory[a] + int(registers[x], 16)
    if temp > 255:
        registers[x] = hex(255)
    else:
        registers[x] = hex(temp)


def SUB_REG_MEM(x, y):
    a = int(y, 16)
    temp = memory[a] - int(registers[x], 16)
    if temp < 0:
        registers[x] = hex(0)
    else:
        registers[x] = hex(temp)


#################################################


def instruction_layout():
    window["_SUBMIT_"].Update(visible=False)
    window["_INITIAL_TEXT_"].Update(visible=False)
    window["_INSTRUCTION_TEXT_"].Update(visible=True)
    window["_INPUT_ERROR_"].Update(visible=False)
    window["_INPUTS_"].Update(visible=False)
    window["_REGISTER_VALUES_"].Update(visible=True)
    window["_INSTRUCTIONS_"].Update(visible=True)
    window["_ADDRESS_CHOICE_NAME_"].Update(visible=True)
    window["_REGISTER_CHOICE_"].Update(visible=True)
    window["_ALLOW_MEMORY_"].Update(visible=True)
    window["_ADDRESS_INFO_"].Update(visible=True)


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


register_memory_input = [[sg.Combo([x for x in registers.keys()], size=5, key="_FIRST_LIST_"),
                          sg.InputText(size=5, key="_MEMORY1_", visible=False)],
                         [sg.Combo([x for x in registers.keys()], size=5, key="_SECOND_LIST_"),
                          sg.InputText(size=5, key="_MEMORY2_", visible=False)]]

address_choice_name = [[sg.Text("First address:")],
                       [sg.Text("Second address:")]]

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

allow_memory = [
    [sg.Checkbox("Allow memory", enable_events=True, default=False, key="_ALLOW_MEMORY_1_")],
    [sg.Checkbox("Allow memory", enable_events=True, default=False, key="_ALLOW_MEMORY_2_")]
]

layout = [
    [sg.Text("\nEnter initial state of Intel 8086 registers in hexadecimal values:", key="_INITIAL_TEXT_"),
     sg.Text("\nChoose instruction and registers for simulation:\n", key="_INSTRUCTION_TEXT_",
             visible=False)],
    [sg.Column(address_choice_name, key="_ADDRESS_CHOICE_NAME_", visible=False),
     sg.Column(register_memory_input, key="_REGISTER_CHOICE_", visible=False),
     sg.Column(allow_memory, key="_ALLOW_MEMORY_", visible=False)],
    [sg.Column(register_names, key="_REGISTER_NAMES_"), sg.Column(inputs, key="_INPUTS_", visible=True),
     sg.Column(register_values, key="_REGISTER_VALUES_", visible=False),
     sg.Column(instructions, key="_INSTRUCTIONS_", visible=False)],
    [[sg.Button('Submit', key='_SUBMIT_')]],
    [sg.Text("For instructions working on single address, first is used.", key="_ADDRESS_INFO_", visible=False)],
    [sg.Text("Inputs not hexadecimal or not 8 bit!", text_color="red", key="_INPUT_ERROR_", visible=False),
     sg.Text("\nInstructions can not be addressed between memory!", text_color="red", key="_ADDRESS_ERROR_",
             visible=False),
     sg.Text("\nWrong memory address!", text_color="red", key="_MEMORY_ERROR_", visible=False)],
]

inputs_given = False

window = sg.Window(title="Simulator of Intel 8086", layout=layout, scaling=3, element_justification='c').Finalize()
window.Maximize()

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
    if values["_ALLOW_MEMORY_1_"]:
        window["_FIRST_LIST_"].Update(visible=False)
        window["_MEMORY1_"].Update(visible=True)
    if values["_ALLOW_MEMORY_2_"]:
        window["_SECOND_LIST_"].Update(visible=False)
        window["_MEMORY2_"].Update(visible=True)
    if not values["_ALLOW_MEMORY_1_"]:
        window["_ADDRESS_ERROR_"].Update(visible=False)
        window["_FIRST_LIST_"].Update(visible=True)
        window["_MEMORY1_"].Update(visible=False)
    if not values["_ALLOW_MEMORY_2_"]:
        window["_ADDRESS_ERROR_"].Update(visible=False)
        window["_SECOND_LIST_"].Update(visible=True)
        window["_MEMORY2_"].Update(visible=False)
    if values["_ALLOW_MEMORY_1_"] and values["_ALLOW_MEMORY_2_"]:
        window["_ADDRESS_ERROR_"].Update(visible=True)
    if values["_FIRST_LIST_"] != "" and values["_SECOND_LIST_"] != "" \
            and not values["_ALLOW_MEMORY_1_"] and not values["_ALLOW_MEMORY_2_"]:
        if event == "MOV":
            MOV(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
        if event == "XCHG":
            XCHG(values["_FIRST_LIST_"], values["_SECOND_LIST_"])
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
    if values["_FIRST_LIST_"] != "" and not values["_ALLOW_MEMORY_1_"]:
        if event == "NOT":
            NOT(values["_FIRST_LIST_"])
        if event == "INC":
            INC(values["_FIRST_LIST_"])
        if event == "DEC":
            DEC(values["_FIRST_LIST_"])
    if values["_MEMORY1_"] != "" and values["_ALLOW_MEMORY_1_"]:
        if correct_memory(values["_MEMORY1_"]):
            window["_MEMORY_ERROR_"].Update(visible=False)
            if event == "NOT":
                NOT_MEM(values["_MEMORY1_"])
            if event == "INC":
                INC_MEM(values["_MEMORY1_"])
            if event == "DEC":
                DEC_MEM(values["_MEMORY1_"])
        if not correct_memory(values["_MEMORY1_"]):
            window["_MEMORY_ERROR_"].Update(visible=True)
    if values["_ALLOW_MEMORY_1_"] and not values["_ALLOW_MEMORY_2_"] \
            and values["_MEMORY1_"] and values["_SECOND_LIST_"]:
        if correct_memory(values["_MEMORY1_"]):
            if event == "MOV":
                MOV_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
            if event == "XCHG":
                XCHG_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
            if event == "AND":
                AND_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
            if event == "OR":
                OR_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
            if event == "XOR":
                XOR_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
            if event == "ADD":
                ADD_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
            if event == "SUB":
                SUB_MEM_REG(values["_MEMORY1_"], values["_SECOND_LIST_"])
    if values["_ALLOW_MEMORY_2_"] and not values["_ALLOW_MEMORY_1_"] \
            and values["_MEMORY2_"] and values["_FIRST_LIST_"]:
        if correct_memory(values["_MEMORY2_"]):
            window["_MEMORY_ERROR_"].Update(visible=False)
            if event == "MOV":
                MOV_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
            if event == "XCHG":
                XCHG_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
            if event == "AND":
                AND_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
            if event == "OR":
                OR_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
            if event == "XOR":
                XOR_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
            if event == "ADD":
                ADD_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
            if event == "SUB":
                SUB_REG_MEM(values["_FIRST_LIST_"], values["_MEMORY2_"])
        if not correct_memory(values["_MEMORY2_"]):
            window["_MEMORY_ERROR_"].Update(visible=True)
    update_shown_values()
window.close()