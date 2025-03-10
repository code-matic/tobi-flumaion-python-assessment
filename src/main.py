''' Main entry for the application as a script. '''
from datetime import datetime
from src.repository.employee import EmployeeRepository
from src.services.retirement_service import RetirementService
from src.utils.logger import setup_logger

# 
logger = setup_logger(__name__)


def main():
    logger.info("Starting retirement computation script.")
    computation_date = datetime.today().date()
    logger.debug(f"Computation Date: {computation_date}")
    employee_repository = EmployeeRepository()
    retirement_service = RetirementService(employee_repository)

    retiring_employees = retirement_service.get_retiring_employees(computation_date)
    total_salary = retirement_service.calculate_total_salary(retiring_employees)
    logger.debug(f"Retiring Employees: {[emp.model_dump() for emp in retiring_employees]}")
    logger.info(f"Total Salary Liability: {total_salary}")

    print(f"Computation Date: {computation_date}")
    print("Retiring Employees:")
    for emp in retiring_employees:
        print(emp.model_dump())
    print(f"Total Salary Liability: {total_salary}")

if __name__ == "__main__":
    main()