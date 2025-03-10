from datetime import datetime
from src.schemas.employee import Employee
from src.core.db import load_employee
from src.interfaces.repository import AbstractRepository


class EmployeeRepository(AbstractRepository):
    def __init__(self):
        self._employees = load_employee()

    def create(self, employee: Employee):
        employee.id = str(len(self._employees) + 1)
        self._employees.append(employee)

    def get(self, id: str) -> Employee:
        """Get an employee"""
        employee = [e for e in self._employees if e.id == id]
        if employee:
            return employee[0]
        return None

    def delete(self, id: str):
        """Delete an employee"""
        self._employees = [e for e in self._employees if e.id != id]

    def get_all(self) -> list[Employee]:
        """Return all employees"""
        return self._employees