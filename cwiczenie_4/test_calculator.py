import pytest
from calculator import Calculator

# ── Podstawowe operacje ───────────────────────────────────────────────────────

def test_dodawanie(calc):
    assert calc.add(2, 3) == 5

def test_odejmowanie(calc):
    assert calc.subtract(10, 4) == 6

def test_mnozenie(calc):
    assert calc.multiply(3, 7) == 21

def test_dzielenie(calc):
    assert calc.divide(10, 2) == 5.0

def test_dzielenie_przez_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)

def test_potegowanie(calc):
    assert calc.power(2, 10) == 1024

def test_potegowanie_zera_do_ujemnej(calc):
    with pytest.raises(ValueError):
        calc.power(0, -1)

def test_procent(calc):
    assert calc.percent(25, 100) == 25.0

def test_procent_zero_total(calc):
    with pytest.raises(ZeroDivisionError):
        calc.percent(10, 0)

def test_procent_ujemna_wartosc(calc):
    with pytest.raises(ValueError):
        calc.percent(-5, 100)

# ── Historia ──────────────────────────────────────────────────────────────────

def test_historia_zawiera_wpisy(calc_with_history):
    history = calc_with_history.get_history()
    assert len(history) >= 3

def test_last_result_po_dodawaniu(calc):
    calc.add(7, 3)
    assert calc.last_result() == 10.0

def test_last_result_pusta_historia(calc):
    assert calc.last_result() is None

def test_czyszczenie_historii(calc):
    calc.add(1, 1)
    calc.clear_history()
    assert calc.get_history() == []

# ── Parametryzowane fixtures ──────────────────────────────────────────────────

def test_dodawanie_liczb_dodatnich(calc, positive_number):
    result = calc.add(positive_number, 0)
    assert result == positive_number

def test_mnozenie_przez_zero(calc, positive_number):
    assert calc.multiply(positive_number, 0) == 0

def test_procent_ujemny_total(calc):
    with pytest.raises(ValueError):
        calc.percent(10, -100)