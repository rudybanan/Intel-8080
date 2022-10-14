from itertools import product
allowed_values = list(map(''.join, product('0123456789ABCDEF', repeat=2)))
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


def register_state():
    for register, value in registers.items():
        print(register, "=", value)


def MOV(a, b):
    registers[a] = registers[b]


while run:
    for x in registers:
        registers[x] = input(f"Enter value stored in {x} register: ")
    if registers.values in allowed_values:
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
        print("\nWrong input! Input(s) not a 8 bit number or not hexadecimal!\n")
