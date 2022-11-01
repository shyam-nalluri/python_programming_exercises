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


def to_roman_numeral(arabic_number) -> str:
    """Converts Arabic number to Roman number"""
    if arabic_number == 0:
        return "nulla"
    max_length = len(ARABIC_NUMBERS) - 1
    converted_romans = ""
    while arabic_number != 0:
        if ARABIC_NUMBERS[max_length] <= arabic_number:
            converted_romans += ROMAN_NUMBERS[max_length]
            arabic_number -= ARABIC_NUMBERS[max_length]
        else:
            max_length -= 1
    return converted_romans


roman_arabic_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_arabic_number(roman_numeral: str) -> int:
    """Converts Roman number to Arabic"""
    if roman_numeral == "nulla":
        return 0
    arabic_number = 0
    last = "I"
    for numeral in roman_numeral[::-1]:
        if roman_arabic_numerals[numeral] < roman_arabic_numerals[last]:
            arabic_number -= roman_arabic_numerals[numeral]
        else:
            arabic_number += roman_arabic_numerals[numeral]
        last = numeral
    return arabic_number


if __name__ == "__main__":

    OPTION = input(
        """Choose option below
    --roman
    --numeral\n"""
    )
    try:
        if OPTION == "--roman":
            result = to_roman_numeral(
                int(input("""Enter Arabic number between 1 and 3999: """))
            )
            print(result)
        elif OPTION == "--numeral":
            result = to_arabic_number(input("""Enter Roman number: """).upper())
            print(result)
    except Exception as error:
        print(error)
