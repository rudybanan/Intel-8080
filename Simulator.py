run = True
registers = {"AL": 0,
             "AH": 0,
             "BL": 0,
             "BH": 0,
             "CL": 0,
             "CH": 0,
             "DL": 0,
             "DH": 0,
             }


def registers_hex_and_8bit():
    for register, value in registers.items():
        try:
            int(value, 16)
            return True
        except ValueError:
            return False


def stan_rejestru():
    for register, value in registers.items():
        print(register, "=", value)


def MOV(a, b):
    registers[a] = registers[b]


while run:
    for x in registers:
        registers[x] = input(f"Podaj zawartość rejestru {x}: ")
    if registers_hex_and_8bit():
        print("\nStan początkowy rejestrów procesora Intel8086:")
        stan_rejestru()
        print("\nPodaj nazwę rozkazu dla procesora do symulacji: ")
        rozkaz = input()
        if rozkaz == "MOV":
            print("Podaj pierwszy rejestr rozkazu MOV: ")
            reg1 = input()
            print("Podaj drugi rejestr rozkazu MOV: ")
            reg2 = input()
            MOV(reg2, reg1)
            stan_rejestru()
        else:
            print("Zły rozkaz!")
    else:
        print("\nWrong input! Not hexadecimal or bigger then 8 bit!\n")