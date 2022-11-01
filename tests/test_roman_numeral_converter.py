"""This code tests the running of roman numeral converter"""

from application.roman_numeral_converter import to_arabic_number, to_roman_numeral


def test_to_roman_numeral():
    """Tests the conversion to roman numeral"""
    assert to_roman_numeral(1) == "I"
    assert to_roman_numeral(2008) == "MMVIII"
    assert to_roman_numeral(4) == "IV"
    assert to_roman_numeral(90) == "XC"
    assert to_roman_numeral(3999) == "MMMCMXCIX"


def test_to_arabic_numeral():
    """Tests the conversion to arabic numbers"""
    assert to_arabic_number("I") == 1
    assert to_arabic_number("MMVIII") == 2008
    assert to_arabic_number("IV") == 4
    assert to_arabic_number("XC") == 90
    assert to_arabic_number("MMMCMXCIX") == 3999


def test_to_arabic_number_zero():
    assert to_arabic_number("nulla") == 0


def test_to_roma_numeral_zero():
    assert to_roman_numeral(0) == "nulla"
