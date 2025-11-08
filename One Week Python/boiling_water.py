# Grab first character
unit = input("What unit are you using? ").strip().lower()[0]
temperature = float(input("What temperature is the water? "))

if unit.startswith("f"):
    if temperature == 212:
        print("Water is boiling!")
    else:
        print("Water is not boiling. Must hit 212F")
elif unit.startswith("c"):
    if temperature == 100:
        print("Water is boiling!")
    else:
        print("Water is not boiling. Must hit 100C")
elif unit.startswith("k"):
    if temperature == 373:
        print("Water is boiling!")
    else:
        print("Water is not boiling. Must hit 373K")
else:
    print("Unknown temperate unit!")