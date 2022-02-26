w = int(input('Weight: '))
unit = input('L(bs) or K(g): ')
if unit.upper() == "L":
    m = w * 0.45
    print(f"you are {m} kilos")
else:
    m = w / 0.45
    print(f"you are {m} pounds")