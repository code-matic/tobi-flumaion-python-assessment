from datetime import date
from typing import List
from src.schemas.employee import Employee
from src.repository.employee import EmployeeRepository


class RetirementService:
    def __init__(self, employee_repository: EmployeeRepository, retirement_age: int = 67):
        self.employee_repository = employee_repository
        self.retirement_age = retirement_age
    
    def get_retiring_employees(self, computation_date: date):
        """ Returns a list of employees retiring in the year of the computation_date"""
        employees = self.employee_repository.get_all()
        return [e for e in employees if self._is_retiring(e, computation_date)]
    
    def calculate_total_salary(self, retiring_employees:List[Employee]):
        """Aggregates the total salary of provided employees"""
        return sum([e.salary for e in retiring_employees])

    
    def _is_retiring(self, employee:Employee, computation_date):
        """
        Check if an employee is retiring

        Retirement is considered upon completion of 67 years of age,
        Employee's 67th birthday must be on or before the computation date
        """
        retirement_date = employee.date_of_birth.replace(year=employee.date_of_birth.year + self.retirement_age)
        return retirement_date <= computation_date