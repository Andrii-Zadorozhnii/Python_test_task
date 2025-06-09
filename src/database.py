import sqlite3
import os
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)
DB_PATH = os.getenv("DB_PATH", "cpa_data.db")


@contextmanager
def db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    with db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_stats (
                date TEXT NOT NULL,
                campaign_id TEXT NOT NULL,
                spend REAL DEFAULT 0,
                conversions INTEGER DEFAULT 0,
                cpa REAL,
                PRIMARY KEY (date, campaign_id)
        """
        )
        logger.info("Database initialized")


def upsert_data(data):
    with db_connection() as conn:
        cursor = conn.cursor()
        for record in data:
            cursor.execute(
                """
                INSERT INTO daily_stats (date, campaign_id, spend, conversions, cpa)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(date, campaign_id) DO UPDATE SET
                    spend = excluded.spend,
                    conversions = excluded.conversions,
                    cpa = excluded.cpa
            """,
                (
                    record["date"],
                    record["campaign_id"],
                    record.get("spend", 0),
                    record.get("conversions", 0),
                    record.get("cpa"),
                ),
            )
        conn.commit()
        logger.info(f"Upserted {len(data)} records")
