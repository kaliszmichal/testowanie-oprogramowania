import pytest
from user_repository import UserRepository

@pytest.fixture
def repo():
    """Pusta baza danych — scope: function (domyślny)."""
    repository = UserRepository(":memory:")
    yield repository
    repository.close()

@pytest.fixture(scope="module")
def repo_with_data():
    """Baza z 3 użytkownikami — scope: module."""
    repository = UserRepository(":memory:")
    repository.add_user("Anna Kowalska", "anna@example.com", 28)
    repository.add_user("Jan Nowak", "jan@example.com", 35)
    repository.add_user("Maria Wiśniewska", "maria@example.com", 22)
    yield repository
    repository.close()