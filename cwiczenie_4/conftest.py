import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    """Nowy kalkulator dla każdego testu (function scope)."""
    return Calculator()

@pytest.fixture(scope="module")
def calc_with_history():
    """Kalkulator z historią — współdzielony w module."""
    c = Calculator()
    c.add(10, 5)
    c.subtract(10, 3)
    c.multiply(4, 3)
    return c

@pytest.fixture(params=[1, 5, 10, 100])
def positive_number(request):
    """Parametryzowany fixture — różne liczby dodatnie."""
    return request.param

@pytest.fixture(params=[-1, -5, -10])
def negative_number(request):
    """Parametryzowany fixture — różne liczby ujemne."""
    return request.param