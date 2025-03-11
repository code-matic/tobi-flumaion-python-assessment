from datetime import datetime
from src.schemas.employee import Employee, BaseEmployee
from src.interfaces.repository import AbstractRepository
from src.utils.logger import setup_logger
from src.models.employee import EmployeeORM
from sqlalchemy.orm import Session

logger = setup_logger(__name__)
class EmployeeRepository(AbstractRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, employee: BaseEmployee)-> Employee:
        db_employee = EmployeeORM(**employee.model_dump())
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return Employee.model_validate(db_employee)
    

    def get(self, id: int) -> Employee:
        """Get an employee"""
        db_employee = self.db.query(EmployeeORM).filter(EmployeeORM.id == id).first()
        if db_employee:
            return Employee.model_validate(db_employee)
        return None
       

    def delete(self, id: int):
        """Delete an employee"""
        db_employee = self.db.query(EmployeeORM).filter(EmployeeORM.id == id).first()
        if db_employee:
            self.db.delete(db_employee)
            self.db.commit()

    def get_all(self) -> list[Employee]:
        """Return all employees"""
        db_employees = self.db.query(EmployeeORM).all()
        return [Employee.model_validate(emp) for emp in db_employees]