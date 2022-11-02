import click


@click.group
def mycommands():
    pass


arabic_numerals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman_numerals = [
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


@click.command()
@click.option(
    "--arabic_number",
    prompt="Enter Arabic Numeral",
    default=1,
    help="#Converts Arabic to Roman numeral",
)
def to_roman_numeral(arabic_number) -> str:
    """Converts Arabic number to Roman number"""
    if arabic_number == 0:
        return "nulla"
    max_length = len(arabic_numerals) - 1
    converted_romans = ""
    while arabic_number != 0:
        if arabic_numerals[max_length] <= arabic_number:
            converted_romans += roman_numerals[max_length]
            arabic_number -= arabic_numerals[max_length]
        else:
            max_length -= 1
    click.echo(converted_romans)


roman_arabic_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


@click.command()
@click.option(
    "--roman_numeral",
    prompt="Enter Roman Numeral",
    default="I",
    help="#Converts Roman numeral to Arabic",
)
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
    click.echo(arabic_number)


mycommands.add_command(to_arabic_number)
mycommands.add_command(to_roman_numeral)

if __name__ == "__main__":
    mycommands()
