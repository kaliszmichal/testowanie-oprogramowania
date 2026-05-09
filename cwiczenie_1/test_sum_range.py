import pytest
from sum_range import sum_range

# ── Zadanie 1.1 — 10 testów poprawnościowych ──────────────────────────────────

def test_suma_1_do_5():
    assert sum_range(1, 5) == 15

def test_zero_do_zera():
    assert sum_range(0, 0) == 0

def test_ujemne_do_dodatnich():
    assert sum_range(-3, 3) == 0

def test_ujemne_do_ujemnych():
    assert sum_range(-5, -1) == -15

def test_ten_sam_element():
    assert sum_range(10, 10) == 10

def test_klasyczna_suma_gaussa():
    assert sum_range(1, 100) == 5050

def test_zero_do_jeden():
    assert sum_range(0, 1) == 1

def test_minus_jeden_do_zera():
    assert sum_range(-1, 0) == -1

def test_duzy_zakres():
    assert sum_range(100, 200) == 15150

def test_zero_do_dziesiec():
    assert sum_range(0, 10) == 55

# ── Zadanie 1.2 — testy wyjątków ─────────────────────────────────────────────

def test_a_wieksze_od_b_rzuca_value_error():
    with pytest.raises(ValueError):
        sum_range(10, 5)

def test_argument_float_rzuca_type_error():
    with pytest.raises(TypeError):
        sum_range(1.5, 5)

def test_argument_string_rzuca_type_error():
    with pytest.raises(TypeError):
        sum_range("1", 5)

def test_argument_none_rzuca_type_error():
    with pytest.raises(TypeError):
        sum_range(None, 5)

# ── Zadanie 1.3 — testy parametryzowane ──────────────────────────────────────

@pytest.mark.parametrize("a, b, oczekiwany", [
    (1,   5,   15),
    (0,   0,    0),
    (-3,  3,    0),
    (-5, -1,  -15),
    (10, 10,   10),
    (1,  100, 5050),
    (0,   1,    1),
    (-1,  0,   -1),
    (100, 200, 15150),
    (0,  10,   55),
])
def test_sum_range_parametryzowany(a, b, oczekiwany):
    assert sum_range(a, b) == oczekiwany