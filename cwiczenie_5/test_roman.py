import pytest
from roman import RomanNumeral

def test_jeden_to_I():
    assert RomanNumeral.to_roman(1) == "I"