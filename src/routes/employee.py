from fastapi import APIRouter, Depends

from src.repository.employee import EmployeeRepository
from src.services.retirement_service import RetirementService
from src.interfaces.repository import AbstractRepository
from src.schemas.employee import BaseEmployee, CreateEmployeeResponse, RetirementResponse, RetirementData
from datetime import datetime
from src.utils.utils import api_response
from sqlalchemy.orm import Session
from src.core.db import get_db




employee_router = APIRouter()

def get_employee_repository(db:Session = Depends(get_db)) -> AbstractRepository:
    return EmployeeRepository(db)


def get_retirement_service(
    employee_repository: AbstractRepository = Depends(get_employee_repository)  
):
    return RetirementService(employee_repository)


@employee_router.get("/list-retiring-employees", response_model=RetirementResponse)
async def get_retiring_employees(retirement_service: RetirementService = Depends(get_retirement_service)):
    """
    Return a JSON response of employees retiring in the current year
    
    """
    computation_date = datetime.today().date()
    retiring_employees = retirement_service.get_retiring_employees(computation_date)
    total_salary = retirement_service.calculate_total_salary(retiring_employees)
    response = RetirementData(retiring_employees=retiring_employees, total_salary=total_salary)
    return api_response(response)    


@employee_router.post("/new-employee", response_model=CreateEmployeeResponse)
async def add_employee(employee: BaseEmployee, employee_repository: AbstractRepository = Depends(get_employee_repository)):
    """
    Add a new employee to the repository
    """
    new_employee = employee_repository.create(employee)
    return api_response(new_employee)