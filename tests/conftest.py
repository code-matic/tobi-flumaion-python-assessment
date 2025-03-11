import sys
import os
import json
import pytest
import importlib
from datetime import date, datetime
from unittest.mock import patch
from src.schemas.employee import Employee
from src.repository.employee import EmployeeRepository
from src.utils.utils import default_converter


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class MockEmployeeRepository:
    """A mock repository for testing RetirementService."""
    def __init__(self, employees):
        self._employees = employees

    def get_all(self):
        return self._employees

    def create(self, employee: Employee):
        pass

    def get(self, id: str) -> Employee:
        for e in self._employees:
            if e.id == id:
                return e
        return None

    def delete(self, id: str):
        pass

@pytest.fixture
def mock_employees():
    """
    Create a list of mock employees for testing.

     For computation_date = 2025-01-01:
      - Forever (67th birthday: 2025-06-15) should NOT be included.
      - Favour (67th birthday: 2027-01-01) should NOT be included.
      - Goodness (67th birthday: 2024-12-31) SHOULD be included.
    """
    emp1 = Employee(id=1, name="Forever", date_of_birth=date(1958, 6, 15), salary=100000)
    emp2 = Employee(id=2, name="Favour", date_of_birth=date(1960, 1, 1), salary=80000)
    emp3 = Employee(id=3, name="Goodness", date_of_birth=date(1957, 12, 31), salary=85000)
    return [emp1, emp2, emp3]

# A fixed datetime class to override datetime.today() in the endpoint.
class FixedDateTime(datetime):
    @classmethod
    def today(cls):
        # Return a fixed date after Employee 3's 67th birthday.
        return cls(2025, 1, 2)




@pytest.fixture
def employee_repository(mock_employees, monkeypatch):
    """
    Fixture to create an EmployeeRepository instance using a fake load_employee.
    """
    monkeypatch.setattr("src.repository.employee.EMPLOYEES_DB", mock_employees)
    yield EmployeeRepository()



@pytest.fixture
def test_db(tmp_path, monkeypatch, mock_employees):
    test_file = tmp_path / "employees_test.json"
    test_file.write_text(json.dumps([emp.model_dump() for emp in mock_employees], indent=2, default=default_converter))
    # Patch the DATA_FILE variable in src/core/db so that the repository loads from our test file.
    monkeypatch.setattr("src.core.db.DATA_FILE", str(test_file))
    import src.repository.employee as emp_mod
    importlib.reload(emp_mod)
    return str(test_file)