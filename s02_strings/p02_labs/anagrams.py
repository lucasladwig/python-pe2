# Your task is to write a program which:
# * asks the user for two separate texts;
# * checks whether, the entered texts are anagrams and prints the result.

# Note:
# * assume that two empty strings are not anagrams;
# * treat upper- and lower-case letters as equal;
# * spaces are not taken into account during the check - treat them as non-existent


def is_anagram(txt_1: str, txt_2: str) -> str:
    """Checks if the two provided strings are anagrams."""

    txt_1 = txt_1.lower().replace(" ", "")
    txt_2 = txt_2.lower().replace(" ", "")

    if (len(txt_1) < 1 or len(txt_2) < 1 or len(txt_1) != len(txt_2)):
        return False

    return sorted(txt_1) == sorted(txt_2)


# Start program
user_text_1 = input("Enter first text: ")
user_text_2 = input("Enter second text: ")

if is_anagram(user_text_1, user_text_2):
    print("Anagrams")
else:
    print("Not anagrams")
