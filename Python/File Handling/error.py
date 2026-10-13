# Write a Python program that creates a list of 5 numbers.
# Ask the user for an index number and print the value at that index.
# If the index is out of range, handle the exception and print "Invalid index!".

names = [12, 23, 45, 65, 78]

inp = int(input("Enter a index: "))

try:
    print(names[inp])
except IndexError:
    print("Invalid index!")
finally:
    print("Programme executed")