import pytest
from roman import RomanNumeral

def test_jeden_to_I():
    assert RomanNumeral.to_roman(1) == "I"

@pytest.mark.parametrize("liczba, oczekiwany", [
    (1, "I"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (14, "XIV"),
    (40, "XL"),
    (90, "XC"),
    (399, "CCCXCIX"),
    (1999, "MCMXCIX"),
    (3999, "MMMCMXCIX"),
])
def test_to_roman_parametryzowany(liczba, oczekiwany):
    assert RomanNumeral.to_roman(liczba) == oczekiwany

@pytest.mark.parametrize("n", [0, -1, 4000, 10000])
def test_to_roman_poza_zakresem(n):
    with pytest.raises(ValueError):
        RomanNumeral.to_roman(n)