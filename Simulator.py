registers = {"AL": None,
             "AH": None,
             "BL": None,
             "BH": None,
             "CL": None,
             "CH": None,
             "DL": None,
             "DH": None,
             }


def register_state():
    print("\nInitial state of the registers of Intel 8080 processor: \n")
    for register in registers:
        print(register, "=", registers[register])


def user_input():
    for r in registers:
        registers[r] = input(f"Enter value stored in {r} register: ")


# noinspection PyTypeChecker
def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def MOV(a, b):
    registers[a] = registers[b]


run = True
while run:
    register_state()
    action = int(input(
        "\nEnter action you want to execute:\n\nChange values of the registers - 1\nEnter instruction for program to execute - 2\nQuit - 3\n"))
    if action == 1:
        wrong_inputs = True
        while wrong_inputs:
            user_input()
            if inputs_hex_and_8_bit():
                wrong_inputs = False
            else:
                print("\nInputs not hexadecimal or not 8 bit!")
    elif action == 2:
        instruction = input("\nEnter instruction name for simulation: ")
        if instruction == "MOV":
            reg1 = input("Enter first register for MOV instruction: ")
            reg2 = input("Enter second register for MOV instruction: ")
            if reg1 and reg2 in registers:
                MOV(reg2, reg1)
                print("\n")
            else:
                print("\nWrong registers!\n")
        else:
            print("Wrong instruction!")
    elif action == 3:
        run = False
    else:
        print("Wrong action!")
