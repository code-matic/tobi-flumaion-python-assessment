from pydantic import BaseModel
from datetime import date


class Employee(BaseModel):
    '''Employee model'''
    id: int
    name: str
    date_of_birth: date
    salary: float