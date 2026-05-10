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

@pytest.mark.parametrize("zapis, oczekiwany", [
    ("I", 1),
    ("IV", 4),
    ("IX", 9),
    ("XIV", 14),
    ("XL", 40),
    ("MCMXCIX", 1999),
    ("MMMCMXCIX", 3999),
])
def test_from_roman_parametryzowany(zapis, oczekiwany):
    assert RomanNumeral.from_roman(zapis) == oczekiwany

@pytest.mark.parametrize("n", [1, 4, 9, 14, 40, 399, 1000, 1999, 3999])
def test_round_trip(n):
    assert RomanNumeral.from_roman(RomanNumeral.to_roman(n)) == n

@pytest.mark.parametrize("s", ["IIII", "VV", "ABCD", "", "123"])
def test_from_roman_niepoprawny_format(s):
    with pytest.raises(ValueError):
        RomanNumeral.from_roman(s)