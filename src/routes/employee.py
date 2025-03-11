from fastapi import APIRouter, Depends
from src.repository.employee import EmployeeRepository
from src.services.retirement_service import RetirementService
from src.interfaces.repository import AbstractRepository
from datetime import datetime
from src.utils.utils import api_response



employee_router = APIRouter()

def get_employee_repository() -> AbstractRepository:
    return EmployeeRepository()


def get_retirement_service(
    employee_repository: AbstractRepository = Depends(get_employee_repository)  
):
    return RetirementService(employee_repository)


@employee_router.get("/list-retiring-employees", response_model=dict)
def get_retiring_employees(retirement_service: RetirementService = Depends(get_retirement_service)):
    """
    Return a JSON response of employees retiring in the current year
    
    """
    computation_date = datetime.today().date()
    retiring_employees = retirement_service.get_retiring_employees(computation_date)
    total_salary = retirement_service.calculate_total_salary(retiring_employees)
    response = {
        "retiring_employees": [retiring_employees],
        "total_salary": total_salary
    }
    return api_response(response)    