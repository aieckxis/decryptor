# Aleckxis Kate v. Bernabe
# BSCpE 1-4

# Problem 2
# Ask the user to input the encrypted text.
encrypted_text = input("Enter a string to descrypt: ")
# Set an empty string for the plain text.
plain_text = ""
# Replace each character in encrypted text with corresponding vowel character.
for char in encrypted_text:
#   if *, change to a
    if char == "*":
        plain_text += "a"
#   if &, change to e
    elif char == "&":
        plain_text += "e"
#   if #, change to i
    elif char == "#":
        plain_text += "i"
#   if +, change to o
    elif char == "+":
        plain_text += "o"
#   if !, change to u
    elif char == "!":
        plain_text += "u"
    else:
        plain_text += char
# Read the encrypted text
import time
for i in range(1, 101):
    print(f"\r\033[31mDecrypting... {i}%\033[0m", end='', flush=True)
    time.sleep(0.03)
# Display the plain text
print("\nPlain text: \033[34m" + plain_text + "\033[0m")
