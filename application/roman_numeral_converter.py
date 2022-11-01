"""This program converts Roman to Arabic numbers and Arabic to Roman numbers between 1 and 3999"""

OPTION = input(
    """Choose option below
--roman
--numeral\n"""
)

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
    max_length = len(ARABIC_NUMBERS) - 1
    converted_romans = ""
    while arabic_number != 0:
        if ARABIC_NUMBERS[max_length] <= arabic_number:
            converted_romans += ROMAN_NUMBERS[max_length]
            arabic_number -= ARABIC_NUMBERS[max_length]
        else:
            max_length -= 1
    return converted_romans


ROMAN_ARABIC_NUMERALS = {
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
    ROMAN_NUMERAL = 0
    last = "I"
    for numeral in roman_numeral[::-1]:
        if ROMAN_ARABIC_NUMERALS[numeral] < ROMAN_ARABIC_NUMERALS[last]:
            ROMAN_NUMERAL -= ROMAN_ARABIC_NUMERALS[numeral]
        else:
            ROMAN_NUMERAL += ROMAN_ARABIC_NUMERALS[numeral]
        last = numeral
    return ROMAN_NUMERAL


try:
    if OPTION == "--roman":
        execute = to_roman_numeral(
            int(input("""Enter Arabic number between 1 and 3999: """))
        )
        print(execute)
    elif OPTION == "--numeral":
        execute = to_arabic_number(input("""Enter Roman number: """).upper())
        print(execute)
except Exception as error:
    print(error)
