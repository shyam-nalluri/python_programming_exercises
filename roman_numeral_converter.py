"""This program converts Roman to Arabic numbers and Arabic to Roman numbers between 1 and 3999"""

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


def to_roman_numeral(arabic_number: int) -> str:
    """Converts Arabic number to Roman number"""
    max_length = len(ARABIC_NUMBERS) - 1
    converted_romans = ""
    while arabic_number != 0:
        if ARABIC_NUMBERS[max_length] <= arabic_number:
            converted_romans += ROMAN_NUMBERS[max_length]
            arabic_number -= ARABIC_NUMBERS[max_length]
        else:
            max_length -= 1
    return converted_romans


def to_arabic_number(roman_numeral: str) -> int:
    """Converts Roman number to Arabic"""
    pass


print(to_roman_numeral(27))
