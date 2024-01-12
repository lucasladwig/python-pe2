# Your task is to write a program which:
# * asks the user for one line of text to encrypt;
# * asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# * prints out the encoded text.
# ! Test your code using the data we've provided.


def caesar_encrypter(text: str, shift: int) -> str:
    """Caesar cipher where the user can define the shift and also preserves case."""

    encrypted_text = ""

    for char in text:
        if char.isalpha():
            code = ord(char) + shift
            if char.isupper():
                char = chr((code - 65) % 26 + 65)
            elif char.islower():
                char = chr((code - 97) % 26 + 97)

        encrypted_text += char

    return encrypted_text


# Test program
try:
    user_text = input("Enter text to encrypt: ")
    shift = int(input("Enter encryption shift (from 1 to 25 inclusive): "))
    if shift < 0 or shift > 25:
        raise ValueError

    print(caesar_encrypter(user_text, shift))

except ValueError or TypeError:
    print("Please insert a positive integer between 1 and 25!")
