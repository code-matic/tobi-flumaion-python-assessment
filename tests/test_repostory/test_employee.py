import pytest
from unittest.mock import patch

import src.core.db as core_db
from datetime import date
from src.schemas.employee import Employee
from src.repository.employee import EmployeeRepository


def test_get_all(employee_repository, mock_employees):
    """
    Test that get_all() returns all the employees from the repository.
    """
    employees = employee_repository.get_all()
    assert len(employees) == len(mock_employees)
    for emp, mock_emp in zip(employees, mock_employees):
        assert emp.id == mock_emp.id
        assert emp.name == mock_emp.name

def test_create(employee_repository):
    """
    Test creating a new employee adds it to the repository,
    and the employee is assigned the correct id.
    """
    initial_employees = employee_repository.get_all()
    initial_count = len(initial_employees)

    new_employee = Employee(id=0,name="Amanda", date_of_birth=date(1998, 7, 7), salary=70000)
    employee_repository.create(new_employee)

    assert new_employee.id == str(initial_count + 1)
    assert len(employee_repository.get_all()) == initial_count + 1

def test_get(employee_repository):
    """
    Test that get() retrieves an employee by id, and returns None for non-existent ids.
    """
    employee = employee_repository.get(1)
    assert employee is not None
    assert employee.id == 1
    assert employee.name == "Forever"

    assert employee_repository.get("999") is None

def test_delete(employee_repository):
    """
    Test that delete() removes the employee from the repository.
    """
    initial_count = len(employee_repository.get_all())
    employee_repository.delete(1)
    new_count = len(employee_repository.get_all())
    assert new_count == initial_count - 1
    
    assert employee_repository.get(1) is None
