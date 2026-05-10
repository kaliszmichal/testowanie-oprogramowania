class Calculator:
    """Kalkulator z historią operacji."""

    def __init__(self):
        self._history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero.")
        result = a / b
        self._history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base: float, exp: float) -> float:
        if exp < 0 and base == 0:
            raise ValueError("Nie można potęgować zera do ujemnej potęgi.")
        result = base ** exp
        self._history.append(f"{base} ^ {exp} = {result}")
        return result

    def percent(self, value: float, total: float) -> float:
        if total == 0:
            raise ZeroDivisionError("Podstawa procentu nie może wynosić zero.")
        if value < 0 or total < 0:
            raise ValueError("Wartości muszą być nieujemne.")
        result = (value / total) * 100
        self._history.append(f"{value} % {total} = {result}")
        return result

    def get_history(self) -> list:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()

    def last_result(self):
        if not self._history:
            return None
        last = self._history[-1]
        return float(last.split("=")[-1].strip())