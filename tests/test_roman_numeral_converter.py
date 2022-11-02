"""This code tests the application roman numeral converter"""

from application.roman_numeral_converter import to_arabic_number, to_roman_numeral


def test_to_roman_numeral_1():
    """Tests the conversion to roman numeral"""
    assert to_roman_numeral(1) == "I"


def test_to_roman_numeral_2008():
    assert to_roman_numeral(2008) == "MMVIII"


def test_to_roman_numeral_4():
    assert to_roman_numeral(4) == "IV"


def test_to_roman_numeral_90():
    assert to_roman_numeral(90) == "XC"


def test_to_roman_numeral_3999():
    assert to_roman_numeral(3999) == "MMMCMXCIX"


""" Test to check conversion to arabic numbers"""


def test_to_arabic_numeral_I():
    """Tests the conversion to arabic numbers"""
    assert to_arabic_number("I") == 1


def test_to_arabic_numeral_MMVIII():
    assert to_arabic_number("MMVIII") == 2008


def test_to_arabic_numeral_IV():
    assert to_arabic_number("IV") == 4


def test_to_arabic_numeral_XC():
    assert to_arabic_number("XC") == 90


def test_to_arabic_numeral_MMMCMXCIX():
    assert to_arabic_number("MMMCMXCIX") == 3999


def test_to_arabic_number_zero():
    assert to_arabic_number("nulla") == 0


def test_to_roma_numeral_zero():
    assert to_roman_numeral(0) == "nulla"
