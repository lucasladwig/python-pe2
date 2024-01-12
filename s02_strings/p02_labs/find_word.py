# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?
# For example:
# * if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# * if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

# Hints:
# * you should use the two-argument variants of the pos() functions inside your code;
# * don't worry about case sensitivity.


def find_word_in_sequence(word: str, sequence: str) -> bool:
    """Find if all letters in a word can be found, in order, within a string."""

    pos = 0

    for char in word:
        pos = sequence.find(char, pos)
        if pos == -1:
            return "No"

    return "Yes"


# Run program
word = input("Enter word to find: ").lower()
sequence = input("Enter letter sequence: ").lower()

print(find_word_in_sequence(word, sequence))
