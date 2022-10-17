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
    for register in registers:
        print(register, "=", registers[register])


def user_input():
    print("\nEnter values stored in registers.\n")
    for r in registers:
        registers[r] = input(f"Enter value stored in {r} register: ")
    print("\nInitial state of the registers of Intel 8080 processor: \n")
    register_state()
    print(inputs_hex_and_8_bit())


# noinspection PyTypeChecker
def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


user_input()
