# Your task is to write a program which:
# * asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY\)
# * outputs the Digit of Life for the date.


def digit_of_life(birthday: int) -> int:
    while birthday > 9:
        birthday = str(birthday)

        birthday = sum([int(digit) for digit in birthday])
    
    return birthday


# Run program
try:
    birthday = int(input("Enter your birthday in a YYYYMMDD format: "))

    print(f"Your digit of life is: {digit_of_life(birthday)}")

except TypeError:
    print("Please enter your birthday using digits only.")
