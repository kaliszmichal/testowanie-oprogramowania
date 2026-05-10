from datetime import datetime

class FileLogger:
    """Zapisuje logi do pliku tekstowego ze znacznikiem czasu."""

    def __init__(self, filepath: str):
        self.filepath = filepath

    def log(self, message: str) -> None:
        """Dopisuje wpis do pliku w formacie: [YYYY-MM-DD HH:MM:SS] message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(entry)

    def read_logs(self) -> list:
        """Zwraca listę wpisów z pliku (każda linia jako element)."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            return []