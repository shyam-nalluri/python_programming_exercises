"""This program converts Roman numbers numbers to Hindu Arabic between 1 and 3999"""


def to_roman_numeral(arabic_number: int) -> str:

    ARABIC_NUMBERS = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    ROMAN_NUMBERS = [
        "I",
        "IV",
        "V",
        "IX",
        "X",
        "XL",
        "L",
        "XC",
        "C",
        "CD",
        "D",
        "CM",
        "M",
    ]
    max_length = len(ARABIC_NUMBERS) - 1
    converted_romans = ""
    while arabic_number != 0:
        if ARABIC_NUMBERS[max_length] <= arabic_number:
            converted_romans += ROMAN_NUMBERS[max_length]
            arabic_number -= ARABIC_NUMBERS[max_length]
        else:
            max_length -= 1
    return converted_romans


print(to_roman_numeral(2666))
