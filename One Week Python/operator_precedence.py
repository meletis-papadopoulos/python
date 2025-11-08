# NOT
# AND
# OR

day = "Tuesday"
is_veteran = False # True
age = 56

# Veterans gte in free on Tuesdays
# Infants under 2 get in for free always
gets_in_for_free = age <= 2 or is_veteran and day == "Tuesday"

if gets_in_for_free:
    print("You get in for free today!")

if not gets_in_for_free:
    print("You have to buy a ticket!")