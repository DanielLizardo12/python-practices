# STRINGS

# Basics-------------
my_string = "abcdefg"

# Indexing--------------------------------------------------------------------------------------
print(my_string[3]) # Index in Python starts at position 0 so position 3 will be the 4th element
print(my_string[-1]) # Index -1 is the last position in arrays

# Slicing------------------------------------------------------
print(my_string[2:]) # Start in position 2 end in last position
print(my_string[:3]) # Does not include las position mentioned
print(my_string[2:5])
print(my_string[:]) # All
print(my_string[::1]) # All with 1 steps
print(my_string[::2]) # All with 2 steps

# Basic Methods------------------
x = my_string.upper() # Uppercase
print(x)

x = my_string.lower() # Lowercase
print(x)

x = my_string.capitalize() # First Letter is uppercase
print(x)

x = my_string.split("e") # The string will split when it encounters "e"
print(x)

my_string = "Hello world"
x = my_string.split() # If not specified it will split when it encounters a blank space
print(x)

# Print Formatting----------------------------------------------------------------------------------------------------------
x = "Insert another string here {}".format("insert me") # Using format() you can insert a string in another string inside {}
print(x)

x = "Item One: {y} Item Two: {z}".format(z = "dog", y = "cat") # You can also asign variables if you want to insert the string in a non linear order
print(x)
