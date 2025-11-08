import datetime
year = input("What year were you born in? ")

if not year.isnumeric():
    print("That isn't a number. Try again please!")
else:
    year = int(year)
    current_year = datetime.date.today().year - year
    print(f"You were born {current_year} years ago!")