from src.ldap_client import fetch_employees_from_ldap
from src.database import clear_employees, insert_employees


def sync_ldap_to_postgres():
    employees = fetch_employees_from_ldap()

    clear_employees()
    insert_employees(employees)