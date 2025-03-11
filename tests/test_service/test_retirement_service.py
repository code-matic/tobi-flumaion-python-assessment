import pytest
from datetime import date
from src.schemas.employee import Employee
from src.services.retirement_service import RetirementService
from tests.conftest import MockEmployeeRepository


@pytest.fixture
def retirement_service(mock_employees):
    """Create a RetirementService instance using the mock repository."""
    mock_employee_repo = MockEmployeeRepository(mock_employees)
    return RetirementService(employee_repository=mock_employee_repo, retirement_age=67)


def test_get_retiring_employees(retirement_service):
    """
    Test that only employees whose 67th birthday is on or before the
    computation date are returned.
    For computation_date = 2025-01-01:
      - Forever (67th birthday: 2025-06-15) should NOT be included.
      - Favour (67th birthday: 2027-01-01) should NOT be included.
      - Goodness (67th birthday: 2024-12-31) SHOULD be included.
    """
    computation_date = date(2025, 1, 1)
    retiring_employees = retirement_service.get_retiring_employees(computation_date)

    assert len(retiring_employees) == 1
    assert retiring_employees[0].name == "Goodness"


def test_calculate_total_salary(retirement_service, mock_employees):
    """
    Test that calculate_total_salary returns the sum of the salaries
    of a provided list of employees.
    """
    total_salary = retirement_service.calculate_total_salary(mock_employees)
    expected_salary = sum(emp.salary for emp in mock_employees)
    assert total_salary == expected_salary


def test_borderline_retirement():
    """
    Test the borderline case where an employee's 67th birthday is exactly
    on the computation date. The employee should be considered as retiring.

    For example, if an employee is born on 1958-01-01, then their 67th birthday
    is 2025-01-01.
    """
    emp = Employee(id="4", name="Derek", date_of_birth=date(1958, 1, 1), salary=110000)
    mock_employee_repo = MockEmployeeRepository([emp])
    service = RetirementService(employee_repository=mock_employee_repo, retirement_age=67)
    computation_date = date(2025, 1, 1)
    retiring_employees = service.get_retiring_employees(computation_date)

    assert len(retiring_employees) == 1
    assert retiring_employees[0].name == "Derek"
