import sqlite3
from typing import Optional

class UserRepository:
    def __init__(self, db_path: str = ":memory:"):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self) -> None:
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                age INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def add_user(self, name: str, email: str, age: int) -> int:
        try:
            cursor = self.connection.execute(
                "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (name, email, age)
            )
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Użytkownik z e-mailem '{email}' już istnieje.")

    def get_user(self, user_id: int) -> Optional[dict]:
        row = self.connection.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_all_users(self) -> list[dict]:
        rows = self.connection.execute("SELECT * FROM users").fetchall()
        return [dict(r) for r in rows]

    def update_age(self, user_id: int, new_age: int) -> bool:
        cursor = self.connection.execute(
            "UPDATE users SET age = ? WHERE id = ?", (new_age, user_id)
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def delete_user(self, user_id: int) -> bool:
        cursor = self.connection.execute(
            "DELETE FROM users WHERE id = ?", (user_id,)
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def close(self) -> None:
        self.connection.close()