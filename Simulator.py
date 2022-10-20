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
    print("\nInitial state of the registers of Intel 8086 processor: \n")
    for register in registers:
        print(register, "=", registers[register])


def user_input():
    for r in registers:
        registers[r] = input(f"Enter value stored in {r} register: ").upper()


# noinspection PyTypeChecker
def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def MOV(a, b):
    registers[a] = registers[b]


def XCHG(x, y):
    registers[x], registers[y] = registers[y], registers[x]


run = True
while run:
    register_state()
    try:
        action = int(input("\nEnter action you want to execute:\n\nChange values of the registers - 1\nEnter instruction for program to execute - 2\nQuit - 3\n\n"))
        if action == 1:
            wrong_inputs = True
            while wrong_inputs:
                user_input()
                if inputs_hex_and_8_bit():
                    wrong_inputs = False
                else:
                    print("\nInputs not hexadecimal or not 8 bit!")
        elif action == 2:
            instruction = int(input("\nChoose instruction for simulation:\nMOV - 1\nXCHG - 2\n\n"))
            if instruction == 1:
                reg1 = input("Enter first register for MOV instruction: ").upper()
                reg2 = input("Enter second register for MOV instruction: ").upper()
                if reg1 and reg2 in registers:
                    MOV(reg2, reg1)
                    print("\n")
                else:
                    print("\nWrong registers!\n")
            elif instruction == 2:
                reg1 = input("Enter first register for XCHG instruction: ")
                reg2 = input("Enter second register for XCHG instruction: ")
                if reg1 and reg2 in registers:
                    XCHG(reg1, reg2)
                else:
                    print("\nWrong registers!\n")
            else:
                print("Wrong instruction!")
        elif action == 3:
            run = False
        else:
            print("Wrong action!")
    except ValueError:
        print("Wrong action!")
