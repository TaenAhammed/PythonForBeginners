weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.lower() == 'l':
    # if (unit == 'L') or (unit == 'l'):
    converted_weight = int(weight) * 0.45
    print(f"Your are {converted_weight} kilos")
# elif (unit == 'K') or (unit == 'k'):
elif unit.lower() == 'k':
    converted_weight = int(weight) / 0.45
    print(f"Your are {converted_weight} pounds")
else:
    print("You've not entered any unit or entered wrong unit.")
