from itertools import product

allowed_values = list(map(''.join, product('0123456789ABCDEF', repeat=2)))

registers = {"AL": 00,
             "AH": 00,
             "BL": 00,
             "BH": 00,
             "CL": 00,
             "CH": 00,
             "DL": 00,
             "DH": 00,
             }


def user_input():
    for r in registers:
        registers[r] = input(f"Enter value stored in {r} register: ")
        print(registers.values)


def register_state():
    for register, value in registers.items():
        print(register, "=", value)


def MOV(a, b):
    registers[a] = registers[b]


run = True

while run:
    user_input()
    if registers.values in allowed_values:
        print("\nInitial state of the registers of Intel 8080 processor: \n")
        register_state()
        action = int(input(
            "\nEnter action which u want to execute:\n\nChange values of the registers - 1\nEnter instruction for program to execute - 2\nQuit - 3\n"))
        if action == 1:
            user_input()
        elif action == 2:
            instruction = input("\nEnter instruction name for simulation: ")
            if instruction == "MOV":
                reg1 = input("Enter first register for MOV instruction: ")
                reg2 = input("Enter second register for MOV instruction: ")
                if reg1 and reg2 in registers:
                    MOV(reg2, reg1)
                else:
                    print("\nWrong registers!\n")
            else:
                print("Wrong instruction!")
        elif action == 3:
            run = False
        else:
            print("Wrong action!")
    else:
        print("\nWrong input! Input(s) not a 8 bit number or not hexadecimal!\n")
