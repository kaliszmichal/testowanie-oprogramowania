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
Wejdź do folderu danego ćwiczenia i uruchom:
```bash
pip install pytest pytest-cov pytest-mock
python -m pytest -v
```