import pytest
from application.roman_numeral_converter import to_arabic_number, to_roman_numeral

# print(to_roman_numeral(10))


def test_to_roman_numeral():
    assert to_roman_numeral(1) == "I"
    assert to_roman_numeral(2008) == "MMVIII"
    assert to_roman_numeral(4) == "IV"
    assert to_roman_numeral(90) == "XC"
    assert to_roman_numeral(3999) == "MMMCMXCIX"
