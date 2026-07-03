import os

from dotenv import load_dotenv
from ldap3 import ALL, Connection, Server

load_dotenv()


def fetch_employees_from_ldap():
    server = Server(
        os.getenv("LDAP_HOST", "localhost"),
        port=int(os.getenv("LDAP_PORT", "3890")),
        get_info=ALL,
    )
    bind_dn = os.getenv("LDAP_BIND_DN", "cn=admin,dc=tester,dc=local")
    bind_password = os.getenv("LDAP_BIND_PASSWORD", "sudo")
    search_base = os.getenv("LDAP_SEARCH_BASE", "ou=Employees,dc=tester,dc=local")

    with Connection(server, user=bind_dn, password=bind_password, auto_bind=True) as conn:
        conn.search(
            search_base=search_base,
            search_filter="(objectClass=inetOrgPerson)",
            attributes=["cn", "sn", "mail", "title", "departmentNumber"],
        )

        employees = []
        for entry in conn.entries:
            employees.append(
                {
                    "cn": str(entry.cn),
                    "sn": str(entry.sn),
                    "email": str(entry.mail),
                    "title": str(entry.title),
                    "department": str(entry.departmentNumber),
                }
            )

    return employees
