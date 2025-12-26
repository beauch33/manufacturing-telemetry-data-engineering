import random
import logging
from datetime import datetime, timedelta
from psycopg2.extras import execute_values
from db_connection import get_connection

logging.basicConfig(level=logging.INFO)

def generate_rows(n=10000):
    now = datetime.utcnow()
    for _ in range(n):
        yield (
            f"V{random.randint(1, 50)}",
            random.choice(["temperature", "vibration"]),
            now - timedelta(seconds=random.randint(0, 3600)),
            random.random() * 100,
        )

def main():
    conn = get_connection()
    rows = list(generate_rows(10000))

    with conn.cursor() as cur:
        execute_values(
            cur,
            """
            INSERT INTO sensor_readings
            (vehicle_id, sensor_name, reading_ts, reading_value)
            VALUES %s
            """,
            rows
        )

    conn.commit()
    conn.close()
    logging.info("Inserted %s sensor readings", len(rows))

if __name__ == "__main__":
    main()
