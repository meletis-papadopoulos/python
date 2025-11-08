# Using a for loop
for beer in range(99, 0, -1):
    if beer != 1:
        print(f"{beer} bottles of beer on the wall.")
        print(f"{beer} bottles of beer.")

        if beer == 2:
            print(f"Take one down, pass it around, {beer - 1} bottle of beer on the wall")
        else:
            print(f"Take one down, pass it around, {beer - 1} bottles of beer on the wall")

    else:
        print(f"{beer} bottle of beer on the wall.")
        print(f"{beer} bottle of beer.")
        print(f"Take one down, pass it around, no more bottles of beer on the wall")  

    print("*" * 50)

# Using a while loop
# bottles_of_beer = 99
# while bottles_of_beer > 0:

#     if bottles_of_beer != 1:
#         print(f"{bottles_of_beer} bottles of beer on the wall.")
#         print(f"{bottles_of_beer} bottles of beer.")

#         if bottles_of_beer == 2:
#             print(f"Take one down, pass it around, {bottles_of_beer - 1} bottle of beer on the wall")
#         else:
#             print(f"Take one down, pass it around, {bottles_of_beer - 1} bottles of beer on the wall")

#     else:
#         print(f"{bottles_of_beer} bottle of beer on the wall.")
#         print(f"{bottles_of_beer} bottle of beer.")
#         print(f"Take one down, pass it around, no more bottles of beer on the wall")  

#     print("*" * 50)
#     bottles_of_beer -= 1