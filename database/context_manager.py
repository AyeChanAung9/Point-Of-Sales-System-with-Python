import sqlite3
import os
from other.global_var import get_db_name


class DatabaseContextManager:
    db_folder = 'database'

    def __init__(self):
        db_name = get_db_name()
        self.db_file = os.path.join(self.db_folder, db_name)
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):  # type: ignore
        if self.connection is not None:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()
