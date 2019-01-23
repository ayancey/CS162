# This script uses the keyboard module written by Christian Howard
# It implements basic file I/O by allowing the user to read and write keys to disk.
# Tests could be used in Christian's module to make sure that keys are named what they're supposed to,
# and that the keys act like you would expect (can't be re-pressed, or re-depressed).

# Difficult CS topics:
# When to use OOP, and when not to use it. I don't personally like some of the ways professors teach this.
# I notice a lot of students implementing classes and inheritance when it's not necessary.
# Especially with Python, I think students should learn how OOP assists design.

from keyboard import Keyboard

new_keyboard = Keyboard()

# Attempt to load keys from file, if it exists
# this could be a method if we needed to load keys from the file more than once
try:
    with open("keys.txt") as f:
        # each key is split by a new line character
        for key in f.read().split("\n"):
            if key:
                new_keyboard.add_key(key)
except FileNotFoundError:
    print("Save file not found, no keys added")


# Add keys from user input, until user types 'exit'
while True:
    new_key = input("Add new key to keyboard (type 'exit' to save and quit): ")

    if new_key.strip().lower() == "exit":
        with open("keys.txt", "w") as f:
            for key in new_keyboard.keys:
                f.write(key + "\n")
        print("Saved!")
        break
    else:
        new_keyboard.add_key(new_key)
