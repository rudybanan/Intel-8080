


def NOT(x):
    temp = ~int(registers[x], 16)
    registers[x] = hex(temp)


reg = "DH"
print(NOT(reg))
