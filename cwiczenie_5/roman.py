class RomanNumeral:
    _VALUES = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I"),
    ]

    _ROMAN_VALUES = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    # Symbole które mogą wystąpić max 3 razy
    _MAX_REPEAT = {"I": 3, "X": 3, "C": 3, "M": 3, "V": 1, "L": 1, "D": 1}

    @staticmethod
    def to_roman(n: int) -> str:
        if not isinstance(n, int) or not (1 <= n <= 3999):
            raise ValueError(f"Liczba musi być całkowita z zakresu 1-3999, otrzymano: {n}")
        result = ""
        for value, symbol in RomanNumeral._VALUES:
            while n >= value:
                result += symbol
                n -= value
        return result

    @staticmethod
    def from_roman(s: str) -> int:
        if not isinstance(s, str) or not s:
            raise ValueError("Argument musi być niepustym łańcuchem znaków.")
        s = s.upper()

        # Sprawdź powtórzenia
        i = 0
        while i < len(s):
            char = s[i]
            if char not in RomanNumeral._ROMAN_VALUES:
                raise ValueError(f"Nieznany symbol: '{char}'")
            count = 1
            while i + count < len(s) and s[i + count] == char:
                count += 1
            if count > RomanNumeral._MAX_REPEAT[char]:
                raise ValueError(f"Symbol '{char}' powtórzony zbyt wiele razy.")
            i += count

        result = 0
        prev = 0
        for char in reversed(s):
            value = RomanNumeral._ROMAN_VALUES[char]
            if value < prev:
                result -= value
            else:
                result += value
            prev = value

        if not (1 <= result <= 3999):
            raise ValueError(f"Wynik poza zakresem 1-3999: {result}")
        return result