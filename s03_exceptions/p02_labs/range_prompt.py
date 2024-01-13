# Your task is to write a function able to input integer values and to check if they are within a specified range.
# The function should:
# * accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
# * if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
# * if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
# * if the input value is valid, return it as a result.


class OutOfRangeError(Exception):
    """Exception raised for errors in the input value being out of the allowed range."""
    pass


def read_int(prompt: str, min: int, max: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value

            raise OutOfRangeError

        except ValueError:
            print("Error: wrong input")

        except OutOfRangeError:
            print(f"Error: the value is not within permitted range ({min}..{max})")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
