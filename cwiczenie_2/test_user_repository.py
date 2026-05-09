import pytest
from user_repository import UserRepository

# ── CREATE ────────────────────────────────────────────────────────────────────

def test_dodaj_uzytkownika_zwraca_id(repo):
    user_id = repo.add_user("Test User", "test@example.com", 25)
    assert user_id == 1

def test_duplikat_email_rzuca_value_error(repo):
    repo.add_user("User A", "duplikat@example.com", 20)
    with pytest.raises(ValueError):
        repo.add_user("User B", "duplikat@example.com", 30)

# ── READ ──────────────────────────────────────────────────────────────────────

def test_pobierz_uzytkownika_po_id(repo):
    user_id = repo.add_user("Alicja", "alicja@example.com", 30)
    user = repo.get_user(user_id)
    assert user["name"] == "Alicja"
    assert user["email"] == "alicja@example.com"
    assert user["age"] == 30

def test_pobierz_nieistniejacego_zwraca_none(repo):
    assert repo.get_user(9999) is None

def test_pobierz_wszystkich_z_danych(repo_with_data):
    users = repo_with_data.get_all_users()
    assert len(users) == 3

# ── UPDATE ────────────────────────────────────────────────────────────────────

def test_aktualizuj_wiek(repo):
    user_id = repo.add_user("Bob", "bob@example.com", 20)
    result = repo.update_age(user_id, 21)
    assert result is True
    assert repo.get_user(user_id)["age"] == 21

def test_aktualizuj_nieistniejacego_zwraca_false(repo):
    assert repo.update_age(9999, 25) is False

# ── DELETE ────────────────────────────────────────────────────────────────────

def test_usun_uzytkownika(repo):
    user_id = repo.add_user("Carol", "carol@example.com", 25)
    assert repo.delete_user(user_id) is True
    assert repo.get_user(user_id) is None

def test_usun_nieistniejacego_zwraca_false(repo):
    assert repo.delete_user(9999) is False

# ── IZOLACJA ──────────────────────────────────────────────────────────────────

def test_izolacja_baza_jest_pusta_na_starcie(repo):
    """Każde wywołanie fixture 'repo' tworzy nową, pustą bazę."""
    assert repo.get_all_users() == []