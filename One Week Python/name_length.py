first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
full_name = len(first_name) + len(last_name)

average_name_length = 12
nationality = "American"

if full_name > average_name_length:
    print(f"{first_name} {last_name}, is longer than the average {nationality} name")
elif len(full_name) == average_name_length:
    print(f"{first_name} {last_name}, is exactly the average length for {nationality} names")
else:
    print(f"{first_name} {last_name}, is shorter than the average {nationality} name")