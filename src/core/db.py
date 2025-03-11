from src.schemas.employee import Employee
from datetime import datetime
from src.utils.utils import default_converter
import os
import json
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


DATA_FILE = "/tmp/employees.json"


def load_employees_from_file() -> list[Employee]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                logger.error("Failed to load employee data.")
                
                data = []
        return [Employee(**item) for item in data]
    return []


def save_employees_to_file(employees: list[Employee]):
    with open(DATA_FILE, "w") as f:
        json.dump([emp.model_dump() for emp in employees], f, indent=2, default=default_converter)


def load_employee()->list[Employee]:
    # employees = [
    #     Employee(id="1", name="Oluwatobi Akintunlese", date_of_birth=datetime(1990, 1, 1), salary=100000.0),
    #     Employee(id="2", name="Rick Sanchez", date_of_birth=datetime(1955, 5, 20), salary=80000.0),
    #     Employee(id="3", name="Morty Smith", date_of_birth=datetime(2005, 1, 1), salary=75000.0),
    #     Employee(id="4", name="Summer Smith", date_of_birth=datetime(2000, 2, 25), salary=1000.0),
    #     Employee(id="5", name="Beth Smith", date_of_birth=datetime(1958,10 , 12), salary=95000.0),
    #     Employee(id="6", name="Youngen Smith", date_of_birth=datetime(2000, 12, 12), salary=54000.0),
    # ]
    employees = load_employees_from_file()
    return employees
