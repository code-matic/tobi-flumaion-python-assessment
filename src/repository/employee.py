from datetime import datetime
from src.schemas.employee import Employee, BaseEmployee
from src.core.db import load_employee
from src.interfaces.repository import AbstractRepository

EMPLOYEES_DB = load_employee()
class EmployeeRepository(AbstractRepository):

    def __init__(self):
        global EMPLOYEES_DB
        self._employees = EMPLOYEES_DB 

    def create(self, employee: BaseEmployee)-> Employee:
        employee_data = employee.model_dump()
        employee_data["id"] = str(len(self._employees) + 1)
        employee = Employee(**employee_data)
        self._employees.append(employee)
        return employee

    def get(self, id: int) -> Employee:
        """Get an employee"""
        employee = [e for e in self._employees if e.id == id]
        if employee:
            return employee[0]
        return None

    def delete(self, id: int):
        """Delete an employee"""
        self._employees = [e for e in self._employees if e.id != id]

    def get_all(self) -> list[Employee]:
        """Return all employees"""
        return self._employees