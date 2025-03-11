import pytest
from fastapi import FastAPI
from unittest.mock import patch
from fastapi.testclient import TestClient
from tests.conftest import MockEmployeeRepository, FixedDateTime
from src.routes.employee import employee_router
from src.services.retirement_service import RetirementService




@pytest.fixture
def get_retirement_service(employee_repository):
    return RetirementService(employee_repository, retirement_age=67)

@pytest.fixture
def app_with_overrides(employee_repository, monkeypatch):
    app = FastAPI()
    app.include_router(employee_router)
    
    # Override the datetime in the routes so that datetime.today() returns our fixed date.
    monkeypatch.setattr("src.routes.employee.datetime", FixedDateTime)
    
    # Override dependency functions in the routes.
    monkeypatch.setattr("src.routes.employee.get_employee_repository", lambda: employee_repository)
    monkeypatch.setattr("src.routes.employee.get_retirement_service", 
                        lambda: RetirementService(employee_repository, retirement_age=67))
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
    assert len(retiring_list) == 1
    emp = retiring_list[0]
    assert emp["id"] == 3
    assert emp["name"] == "Goodness"
    assert data["total_salary"] == "85000.0" or data["total_salary"] == "85000"



def test_add_employee(client):
    payload = {
        "name": "Test Employee",
        "date_of_birth": "2000-01-01",  
        "salary": 50000
    }
    response = client.post("/new-employee", json=payload)
    assert response.status_code == 200

    data = response.json()["data"]
    assert data["id"] is not None
    assert data["name"] == "Test Employee"
    assert data["date_of_birth"] == "2000-01-01"
    assert data["salary"] == "50000" or data["salary"] == "50000.0"