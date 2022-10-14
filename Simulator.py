run = True
registers = {"AL": 00,
             "AH": 00,
             "BL": 00,
             "BH": 00,
             "CL": 00,
             "CH": 00,
             "DL": 00,
             "DH": 00,
             }


def inputs_hex():
    for value in registers.values():
        try:
            int(value, 16)
            return True
        except ValueError:
            return False


def inputs_8bit():
    for value in registers.values():
        if value <= "ff":
            return True
        else:

            break


def register_state():
    for register, value in registers.items():
        print(register, "=", value)


def MOV(a, b):
    registers[a] = registers[b]


while run:
    for x in registers:
        registers[x] = input(f"Enter value stored in {x} register: ")
    if inputs_hex():
        if inputs_8bit():
            print("\nInitial state of the registers of Intel 8080 processor: \n")
            register_state()
            instruction = input("\nEnter instruction name for simulation: ")
            if instruction == "MOV":
                reg1 = input("Enter first register for MOV instruction: ")
                reg2 = input("Enter second register for MOV instruction: ")
                if reg1 and reg2 in registers:
                    MOV(reg2, reg1)
                else:
                    print("\nWrong registers!\n")
            else:
                print("Wrong instruction")
        else:
            print("\nWrong input! Input(s) not a 8 bit number!\n")
    else:
        print("\nWrong input! Input(s) not hexadecimal!\n")
