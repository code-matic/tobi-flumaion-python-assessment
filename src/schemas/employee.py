from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from datetime import date

class BaseEmployee(BaseModel):
    '''Base Employee model'''
    name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: date
    salary:  Decimal = Field(..., ge=0)


class Employee(BaseEmployee):
    '''Employee model'''
    id: int
    model_config = ConfigDict(from_attributes=True)


class CreateEmployeeResponse(BaseModel):
    '''Create Employee Response model'''
    data: Employee
    code: int

class RetirementData(BaseModel):
    '''Retirement Data model'''
    retiring_employees: list[Employee]
    total_salary: Decimal

class RetirementResponse(BaseModel):
    '''Retirement Response model'''
    data: RetirementData
    code: int