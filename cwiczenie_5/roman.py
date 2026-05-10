class RomanNumeral:
    _VALUES = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I"),
    ]

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