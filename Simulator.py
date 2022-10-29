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
        registers[r] = hex(int(input(f"Enter value stored in {r} register: "), 16))


def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def MOV(a, b):
    registers[a] = registers[b]


def XCHG(x, y):
    registers[x], registers[y] = registers[y], registers[x]


def NOT(x):
    temp = int(registers[x], 16)
    registers[x] = hex(255 - temp)


def INC(x):
    temp = int(registers[x], 16)
    temp += 1
    registers[x] = hex(temp)


def DEC(x):
    temp = int(registers[x], 16)
    temp -= 1
    registers[x] = hex(temp)


def AND(x, y):
    registers[x] = registers[x] & registers[y]


def OR(x, y):
    registers[x] = registers[x] | registers[y]


def XOR(x, y):
    registers[x] = registers[x] ^ registers[y]


def ADD(x, y):
    registers[x] = registers[x] + registers[y]


def SUB(x, y):
    registers[x] = registers[x] - registers[y]


while True:
    register_state()
    try:
        action = int(input(
            "\nEnter action you want to execute:\n\nChange values of the registers - 1\nEnter instruction for program to execute - 2\nQuit - 3\n\n"))
        if action == 1:
            wrong_inputs = True
            while wrong_inputs:
                user_input()
                if inputs_hex_and_8_bit():
                    wrong_inputs = False
                else:
                    print("\nInputs not hexadecimal or not 8 bit!")
        elif action == 2:
            instruction = int(
                input("\nChoose instruction for simulation:\nMOV - 1\nXCHG - 2\nNOT - 3\nINC - 4\nDEC - 5\n\n"))
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
            elif instruction == 3:
                reg = input("Enter register for NOT instruction: ")
                if reg in registers:
                    NOT(reg)
            elif instruction == 4:
                reg = input("Enter register for INC instruction: ")
                if reg in registers:
                    INC(reg)
            elif instruction == 5:
                reg = input("Enter register for INC instruction: ")
                if reg in registers:
                    DEC(reg)
            else:
                print("Wrong instruction!")
        elif action == 3:
            break
        else:
            print("Wrong action!")
    except ValueError:
        print("Wrong action!")

# AND - dwa rejestry 0,1 daje 0 w pierwszym itd dla kazdego bitu
# OR -
# XOR -
# ADD - dodawanie
# SUB - odejmowanie
