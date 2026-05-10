# Testowanie Oprogramowania — Ćwiczenia Laboratoryjne

Repozytorium zawiera rozwiązania ćwiczeń laboratoryjnych z przedmiotu
Testowanie Oprogramowania.

## Technologie
- Python 3.9.6
- pytest
- pytest-cov
- pytest-mock

## Struktura projektu
- `cwiczenie_1/` — Testowanie funkcji sumującej liczby z zakresu
- `cwiczenie_2/` — Testowanie komunikacji z bazą danych
- `cwiczenie_3/` — Mockowanie w testowaniu
- `cwiczenie_4/` — Pokrycie testami i fixtures
- `cwiczenie_5/` — TDD: klasa liczby rzymskiej

## Uruchomienie testów

Utwórz i aktywuj środowisko wirtualne:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install pytest pytest-cov pytest-mock requests
```

Uruchom testy dla wybranego ćwiczenia:
```bash
python -m pytest cwiczenie_1/test_sum_range.py -v
python -m pytest cwiczenie_2/test_user_repository.py -v
python -m pytest cwiczenie_3/test_file_logger.py cwiczenie_3/test_currency_service.py -v
python -m pytest cwiczenie_4/test_calculator.py -v
python -m pytest cwiczenie_5/test_roman.py -v
```