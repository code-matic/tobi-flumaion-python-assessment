import pytest
from fastapi import FastAPI
from unittest.mock import patch
from fastapi.testclient import TestClient
from tests.conftest import MockEmployeeRepository, FixedDateTime
from src.routes.employee import employee_router
from src.services.retirement_service import RetirementService


@pytest.fixture
def get_mock_retirement_service(employee_repository):
    return RetirementService(employee_repository, retirement_age=67)

@pytest.fixture
def app_with_overrides(employee_repository):
    app = FastAPI()
    app.include_router(employee_router)

    # Patch the dependencies in the module where they are used (src.routes.employee)
    with patch("src.routes.employee.get_employee_repository", return_value=employee_repository), \
         patch("src.routes.employee.get_retirement_service", return_value=get_mock_retirement_service):
        yield app

@pytest.fixture
def client(app_with_overrides):
    return TestClient(app_with_overrides)

def test_list_retiring_employees(client):
    """
    Given a fixed repository with two employees, and assuming today's date qualifies only Employee 1,
    the endpoint should return Employee 1 as retiring.
    """
    response = client.get("/list-retiring-employees")
    assert response.status_code == 200

    data = response.json()["data"]
    assert "retiring_employees" in data
    assert "total_salary" in data

    # Check that only one employee is returned as retiring.
    retiring_list = data["retiring_employees"]
    assert isinstance(retiring_list, list)
    # one inner list with one employee (Employee 3).
    assert len(retiring_list) == 1
    inner = retiring_list[0]
    assert isinstance(inner, list)
    assert len(inner) == 1
    emp = inner[0]
    assert emp["id"] == 3
    assert emp["name"] == "Goodness"
    assert data["total_salary"] == 85000