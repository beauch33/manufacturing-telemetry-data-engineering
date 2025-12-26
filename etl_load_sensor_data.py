import argparse
import logging
import psycopg2
from psycopg2.extras import execute_values
import random
from datetime import datetime, timedelta

def get_connection():
    return psycopg2.connect(
        dbname="manuf_telemetry",
        user="postgres",
        password="chante",
        host="localhost",
        port=5432,
    )

def generate_readings(n=10000):
    now = datetime.now()
    for i in range(n):
        yield (
            f"V{random.randint(1, 50)}",
            random.choice(["temperature", "vibration"]),
            now - timedelta(seconds=random.randint(0, 3600)),
            random.random() * 100,
        )

def insert_readings(conn, rows):
    with conn.cursor() as cur:
        execute_values(cur, """
            INSERT INTO sensor_readings (vehicle_id, sensor_name, reading_ts, reading_value)
            VALUES %s
        """, rows)
    conn.commit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=10000)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info("Starting ETL with %s rows", args.rows)

    try:
        insert_readings(get_connection(),generate_readings())
    except Exception as e:
        logging.exception("ETL failed: %s", e)

if __name__ == "__main__":
    main()
