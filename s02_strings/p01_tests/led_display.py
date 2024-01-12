def led_display(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")

    if number < 0:
        raise ValueError("Number must be positive")

    numbers_to_led = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", " # ", " # "],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"],  # 9
    ]

    digits = [int(digit) for digit in str(number)]

    for i in range(5):
        for digit in digits:
            print(numbers_to_led[digit][i], end=" ")
        print()

led_display(80085)