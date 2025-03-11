from sqlalchemy import Column, Integer, String, Date, Float
from src.core.db import Base

class EmployeeORM(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    salary = Column(Float, nullable=False)