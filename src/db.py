import sqlite3
import os
from contextlib import contextmanager

BD_PATH = os.getenv("DB_PATH", "cpa_data.db")


class Database:
    @contextmanager
    def connection(self):
        conn = sqlite3.connect(DB_PATH)
        try:
            yield conn
        finally:
            conn.close()

    def initialize(self):
        with self.connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS daily_stats (
                    date TEXT,
                    compaign_id TEXT,
                    spend TEXT,
                    conversion INTEGER,
                    cpa REAL,
                    PRIMARY KEY (date, compaign_id)
                )
                """
            )

    def upsert_data(self, data):
        with self.connection() as conn:
            cursor = conn.cusros()
            for record in data:
                cursor.execute(
                    """
                    INSERT INTO daily_stats
                    """
                )
