import random as rand
import sys
import time

# LISTS OF CHARACTERS
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "|", "`", "~"]

def get_nonneg_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("Please enter a non-negative integer.")
                continue
            return val
        except ValueError:
            print("Invalid input; please enter an integer.")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled.")
            raise

length = get_nonneg_int("Enter the desired length of your password: ")
upps = get_nonneg_int("Enter the number of uppercase characters you want in your password: ")
nums = get_nonneg_int("Enter the number of numbers you want in your password: ")
syms = get_nonneg_int("Enter the number of symbols you want in your password: ")
lengthDone = 0
password = []

if nums + syms + upps > length:
    excess = nums + syms + upps - length
    while excess > 0 and upps > 0:
        upps -= 1
        excess -= 1
    while excess > 0 and syms > 0:
        syms -= 1
        excess -= 1
    while excess > 0 and nums > 0:
        nums -= 1
        excess -= 1

while len(password) < length:
    if nums > 0:
        password.append(rand.choice(numbers))
        nums -= 1
    elif syms > 0:
        password.append(rand.choice(symbols))
        syms -= 1
    elif upps > 0:
        password.append(rand.choice(uppercase))
        upps -= 1
    else:
        password.append(rand.choice(lowercase))

rand.shuffle(password)
print("".join(password))