from dataclasses import dataclass

@dataclass
class Employee:
    cn: str
    sn: str
    email: str
    title: str
    department: str
    