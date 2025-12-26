import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="manuf_telemetry",
        user="postgres",
        password="chante",
        host="localhost",
        port=5432,
    )
