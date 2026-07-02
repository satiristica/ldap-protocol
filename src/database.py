import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                create table if not exists employees (
                    id serial primary key,
                    cn varchar(255) not null,
                    sn varchar(255) not null,
                    email varchar(255) not null,
                    title varchar(255) not null,
                    department varchar(255)
                );
            """)