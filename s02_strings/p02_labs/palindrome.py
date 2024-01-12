# Your task is to write a program which:
# * asks the user for some text;
# * checks whether the entered text is a palindrome, and prints result.

# Note:
# * assume that an empty string isn't a palindrome;
# * treat upper- and lower-case letters as equal;
# * spaces are not taken into account during the check - treat them as non-existent;
# * there are more than a few correct solutions - try to find more than one.


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    if len(text) == 0:
        return False
    
    text = text.lower().replace(" ", "")

    rev_text = ""

    for i in range(len(text)-1, -1, -1):
        rev_text += text[i]

    return text == rev_text


user_text = input("Enter text to check: ")

print(is_palindrome(user_text))