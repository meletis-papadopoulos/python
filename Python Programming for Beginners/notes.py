my_int = 5
my_float = 3.14
my_string = "Hello"

print(my_int)
print(my_float)
print(my_string)

print(type(my_int))
print(type(my_float))
print(type(my_string))

print( "Addition:" )
print( 5 + 5 )      # 10
print( 5 + 5.0 )    # 10.0 (integer + float = float)

print( "Addition Default Data Types:" )
print( type( 5 + 5 ) )      # <class 'int'>
print( type( 5 + 5.0 ) )    # <class 'float'>

print( "Change Data Types:")
print( float(5 + 5) )       # 10.0
print( int(5 + 5.0) )       # 10

print( "Subtraction:" )
print( 5 - 5 )      # 0
print( 5 - 5.0 )    # 0.0 (integer - float = float)

print( "Multiplication:" )
print( 5 * 5 )      # 25
print( 5 * 5.0 )    # 25.0 (integer * float = float)

print( "Division:" )
print( 5 / 5 )      # 1.0 ( Division always returns float )
print( 5 // 5 )     # 1 (// always returns integer)
print( 5 / 3 )      # 1.6666666666666667
print( 5 // 3 )     # 1 ( // floors the result )

print("Modulo:")
print( 7 % 2 )      # 1 ( If either number is float this returns float )
print( 8 % 2 )      # 0 ( If either number is float this returns float )   

print("Exponent:")
print( 2 ** 3)      # 8 ( If either number is float this returns float )

print("Assignment Operators:")
my_int = 8          
print( my_int )     # 8
my_int += 1 
print( my_int )     # 9 ( += 1.0 would assign a float )
my_int -= 1
print( my_int )     # 8  ( -= 1.0 would assign float )
my_int *= 2
print( my_int )     # 16 ( *= 2.0 would assign float )
my_int /= 2
print( my_int )     # 8.0 ( //= always assigns a float )
my_int //= 2
print( my_int )     # 4.0 ( If my_int was an integer this assigns int )
my_int %= 2          
print (my_int )     # 0.0 ( If both are integers then %= assigns int )
my_int += 2         # 2.0 
my_int **= 3        # (2.0)^3
print( my_int )     # 8.0 ( If both are integers then **= assigns int )

# Comprehensive Comparison Operators Examples

print("Comparing equiality and inequality:")
print("5 == 5 is", 5 == 5) # Outputs: True
print("5 == 4 is", 5 == 4) # Outputs: False
print("5 != 4 is", 5 != 4) # Outputs: True
print("5 != 5 is", 5 != 5) # Outputs: False

print("\nType checking of the comparision result:")
print("Type of (5 == 5) is", type(5 == 5)) # Outputs: <class 'bool'>

print("\nComparisons between different data types:")
print("5 == 5.0 is", 5 == 5.0) # Outputs: True, integer compared with float
print("5 == '5' is", 5 =="5") # Outputs: False, integer compare with string

print("\nComparisons between different data types:")
print("5 == 5.0 is", 5 == 5.0)  # Outputs: True, integer compared with float
print("5 == '5' is", 5 == "5")  # Outputs: False, integer compared with string
print("'5' == '5' is", "5" == "5")  # Outputs: True, string compared with string
print("'5' == '5' with different quotes is", "5" == '5')  # Outputs: True

print("\nGreater and less than comparisons:")
print("5 > 4 is", 5 > 4)   # Outputs: True
print("5 < 4 is", 5 < 4)   # Outputs: False
print("5 > 5 is", 5 > 5)   # Outputs: False
print("5 < 5 is", 5 < 5)   # Outputs: False

print("\nGreater or equal and less or equal comparisons:")
print("5 >= 5 is", 5 >= 5)  # Outputs: True
print("5 <= 5 is", 5 <= 5)  # Outputs: True
print("4 >= 5 is", 4 >= 5)  # Outputs: False
print("4 <= 5 is", 4 <= 5)  # Outputs: True

print("\nString comparisons based on lexicographical order:")
print("'cats' > 'dogs' is", "cats" > "dogs")  # Outputs: False
print("'cats' < 'dogs' is", "cats" < "dogs")  # Outputs: True
print("'bbb' > 'aaa' is", "bbb" > "aaa")    # Outputs: True
print("'BBB' > 'aaa' is", "BBB" > "aaa")    # Outputs: False, case sensitivity affects order
print("'cat2' > 'cat1' is", "cat2" > "cat1")  # Outputs: True, compares '2' and '1' as characters

# Checking comparisons with mixed data types (int and str)
# These will cause a TypeError if uncommented because they are not supported
# print(5 > "5")
# print(5 < "5")
print( "and logical operator:" )
print( True and True )        # True
print( True and False )       # False 
print( False and True )       # False 
print( False and False )      # False 

print( "or logical operator:" )
print( True or True )         # True
print( True or False )        # True 
print( False or True )        # True 
print( False or False )       # False 

# Logical operator order:
# not
# and
# or

print( "Operator precedence example:" )
print( True or not False and False )
# True or (not False) and False
# True or True and False
# True or False
# Output: True

print( "Operator precedence example with parentheses:" )
print( (True or not False) and False )
# (True or not False) and False
# (True or True) and False
# True and False
# Output: False

my_string = 'Hello World!'

# Index:      0  1  2  3  4  5  6  7  8  9  10 11
# Characters: H  e  l  l  o     W  o  r  l  d  !

# Negative Index: -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
# Characters:       H   e   l   l   o       W   o   r   l   d   !

# Print the entire string to see the full content
print(my_string)  # Output: Hello World!

# Print the character at index 8 (9th position in the string)
print(my_string[8])  # Output: r

# Print the last character in the string
print(my_string[-1])  # Output: !

# Print the second-to-last character in the string
print(my_string[-2])  # Output: d

# Print the characters from index 3 to 7 (inclusive of index 3,
# exclusive of index 8), which selects a substring from the
# 4th to the 8th character
print(my_string[3:8])  # Output: lo Wo

# Print the first 8 characters of the string (from the beginning
# to the 8th index, not including the 8th index)
print(my_string[:8])  # Output: Hello Wo

# Print characters from index 3 to the end of the string
print(my_string[3:])  # Output: lo World!

# Print characters from index -9 to -4, counting from the end
# This retrieves characters from the 3rd to 8th index from the left
print(my_string[-9:-4])  # Output: lo Wo

# Print the entire string except for the last 4 characters
# This ends at index -4 (exclusive)
print(my_string[:-4])  # Output: Hello Wo

# Print the last 9 characters from the string
# This starts at index -9 and goes to the end
print(my_string[-9:])  # Output: lo World!

# Print characters from index 3 to the 4th-to-last index (exclusive)
# Index 3 represents the 4th character from the start, and
# index -4 represents the 4th character from the end
print(my_string[3:-4])  # Output: lo Wo

# Define a sample string
my_string = "Hello World"

# Length of the string
length = len(my_string)  # Returns 11

# Check string characteristics
is_lower = my_string.islower()  # Returns False
is_upper = my_string.isupper()  # Returns False
is_alpha = my_string.isalpha()  # Returns False (due to space)
is_digit = my_string.isdigit()  # Returns False
is_alnum = my_string.isalnum()  # Returns False (due to space)
is_space = my_string.isspace()  # Returns False

# Convert string case
lower_str = my_string.lower()  # 'hello world'
upper_str = my_string.upper()  # 'HELLO WORLD'
cap_str = my_string.capitalize()  # 'Hello world'
title_str = my_string.title()  # 'Hello World'
swap_str = my_string.swapcase()  # 'hELLO wORLD'

# Stripping spaces
strip_str = my_string.strip()  # 'Hello World'
lstrip_str = my_string.lstrip()  # 'Hello World  ' (left strip)
rstrip_str = my_string.rstrip()  # '  Hello World' (right strip)

# Prefix and Suffix checks
starts_with_hello = my_string.startswith("Hello")  # True
ends_with_world = my_string.endswith("World")  # True

# Replacing substrings
replaced_str = my_string.replace("World", "Python")  # 'Hello Python'

# Finding substrings
find_world = my_string.find("World")  # Returns 6
find_l = my_string.find("l")  # Returns 2
find_nonexist = my_string.find("abc123")  # Returns -1 (not found)

# Counting substrings
count_l = my_string.count("l")  # Returns 3
count_world = my_string.count("World")  # Returns 1
count_nonexist = my_string.count("abc123")  # Returns 0

# Output examples
print("Original String:", my_string)
print("Lowercase:", lower_str)
print("Uppercase:", upper_str)
print("Title Case:", title_str)
print("Replaced String:", replaced_str)
print("First 'l' found at index:", find_l)
print("Count of 'l':", count_l)

#  Splitting and Joining 
#  ---------------------------------------------------
#  These methods were not covered in the video because
#  they require a knowledge of LISTS.
#
#  Lists will be covered later in the course.
#  ---------------------------------------------------

# .split(separator) splits the string into a list of substrings based on a separator.
print("Split into list:", my_string.split())  # Output: ['Hello', 'World']

# .join(iterable) joins a list of strings into a single string, separated by the specified separator.
words = ['Hello', 'World']
print("Joined list into string:", " ".join(words))  # Output: Hello World

name = "YourName"
print(f"My name is {name}!")
print(f"{name = }")

# Demonstrating various f-string usages with "Hello World"

my_string = "Hello World"

# Basic Usage
# Expected Output: My string says: Hello World
print(f"My string says: {my_string}")

# String Truncation
# Expected Output: Truncated string: Hello
print(f"Truncated string: {my_string:.5}")

# Case Manipulation
# Expected Output: Uppercase: HELLO WORLD
print(f"Uppercase: {my_string.upper()}")
# Expected Output: Lowercase: hello world
print(f"Lowercase: {my_string.lower()}")

# Alignment and Width
# Expected Output: Left aligned within 20 chars: |Hello World        |
print(f"Left aligned within 20 chars: |{my_string:<20}|")
# Expected Output: Right aligned within 20 chars: |        Hello World|
print(f"Right aligned within 20 chars: |{my_string:>20}|")
# Expected Output: Center aligned within 20 chars: |    Hello World    |
print(f"Center aligned within 20 chars: |{my_string:^20}|")

# Character Count
count_l = my_string.count('l')
# Expected Output: Number of 'l' in 'Hello World': 3
print(f"Number of 'l' in '{my_string}': {count_l}")

# Including Special Characters
# Expected Output: Curly braces around the string: {Hello World}
print(f"Curly braces around the string: {{{my_string}}}")
# Expected Output: String in quotes: 'Hello World'
print(f"String in quotes: '{my_string}'")

# Combining with Arithmetic
length = len(my_string)
# Expected Output: Length of 'Hello World' plus 5: 16
print(f"Length of '{my_string}' plus 5: {length + 5}")

# Demonstrating various f-string formatting options in Python

# Fixed point number formatting
# Formats the number to two decimal places
num = 3.14159
print(f"Fixed point number: {num:.2f}")  # Expected Output: Fixed point number: 3.14

# Percentage formatting
# Converts the float to a percentage and formats to two decimal places
completion = 0.756
print(f"Percentage: {completion:.2%}")  # Expected Output: Percentage: 75.60%

# Scientific notation formatting
# Formats the number in scientific notation with two decimal places in the exponent
num_large = 1200.5
print(f"Scientific notation: {num_large:.2e}")  # Expected Output: Scientific notation: 1.20e+03

# Thousands separator formatting
# Formats the integer with commas as thousands separators
population = 123456789
print(f"Thousands separator: {population:,}")  # Expected Output: Thousands separator: 123,456,789

# Alignment formatting
# Demonstrates left, right, and center alignment within a field of 10 characters
name = "Alice"
print(f"Left aligned: {name:<10}")   # Expected Output: Left aligned: Alice     
print(f"Right aligned: {name:>10}")  # Expected Output: Right aligned:      Alice
print(f"Center aligned: {name:^10}") # Expected Output: Center aligned:   Alice   

# Padding with characters
# Pads the number with zeros on the left, making it at least two digits long
day = 5
print(f"Padded number: {day:0>2}")  # Expected Output: Padded number: 05

# Binary, octal, and hexadecimal format
# Formats the integer into binary, octal, and hexadecimal representations
num = 255
print(f"Binary format: {num:b}")         # Expected Output: Binary format: 11111111
print(f"Octal format: {num:o}")          # Expected Output: Octal format: 377
print(f"Hexadecimal format: {num:x}")    # Expected Output: Hexadecimal format: ff

# Date formatting
# Formats a datetime object into a human-readable date and time string
from datetime import datetime
now = datetime.now()
print(f"Formatted date and time: {now:%Y-%m-%d %H:%M}")  # Expected Output: Formatted date and time: 2024-05-21 15:45

Link: https://www.w3schools.com/python/python_string_formatting.asp

