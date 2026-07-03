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
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    cn VARCHAR(255) NOT NULL,
                    sn VARCHAR(255) NOT NULL,
                    email VARCHAR(255),
                    title VARCHAR(255),
                    department VARCHAR(255)
                );
            """)


def get_all_employees():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    id,
                    cn,
                    email,
                    title,
                    department
                FROM employees
                ORDER BY id
            """)

            return cur.fetchall()
        
def clear_employees():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employees")


def insert_employees(employees):
    with get_connection() as conn:
        with conn.cursor() as cur:
            for employee in employees:
                cur.execute(
                    """
                    INSERT INTO employees (
                        cn,
                        sn,
                        email,
                        title,
                        department
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        employee["cn"],
                        employee["sn"],
                        employee["email"],
                        employee["title"],
                        employee["department"],
                    ),
                )

