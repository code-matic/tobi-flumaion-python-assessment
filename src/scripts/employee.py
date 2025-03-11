
from datetime import datetime
from src.repository.employee import EmployeeRepository
from src.services.retirement_service import RetirementService
from src.schemas.employee import BaseEmployee
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def compute_retirement_info(employee_repository: EmployeeRepository):
    """Compute and display retirement information for employees."""
    retirement_service = RetirementService(employee_repository)
    computation_date = datetime.today().date()
    
    retiring_employees = retirement_service.get_retiring_employees(computation_date)
    total_salary = retirement_service.calculate_total_salary(retiring_employees)
    
    logger.info("Retirement computation complete.")
    logger.info(f"Total Salary Liability: {total_salary}")
    
    print(f"Computation Date: {computation_date}")
    print("Retiring Employees:")
    for emp in retiring_employees:
        print(emp.model_dump())
    print(f"Total Salary Liability: {total_salary}")

def add_new_employee(employee_repository: EmployeeRepository, args):
    """Add a new employee using provided command-line arguments."""
    try:
        dob = datetime.strptime(args.date_of_birth, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Create a new BaseEmployee from provided data.
    new_employee_data = {
         "name": args.name,
         "date_of_birth": dob,
         "salary": args.salary
    }
    new_employee = employee_repository.create(BaseEmployee(**new_employee_data))
    logger.info(f"New employee added: {new_employee.model_dump()}")
    print("New employee added:")
    print(new_employee.model_dump())
