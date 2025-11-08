day = input("What day of the week is it? ")

if day.lower() == "saturday" or day.lower() == "sunday":
    print(f"It's {day.capitalize()}, so it's weekend!")
else:
    print(f"{day.capitalize()}, is a workday.")