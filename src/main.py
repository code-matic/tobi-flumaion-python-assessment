''' Main entry for the application as a script. '''
import argparse
from src.core.db import SessionLocal, engine, Base
from src.repository.employee import EmployeeRepository
from src.services.retirement_service import RetirementService
from src.utils.logger import setup_logger
from src.scripts.employee import compute_retirement_info, add_new_employee

# 
logger = setup_logger(__name__)
Base.metadata.create_all(bind=engine)

def main():
    parser = argparse.ArgumentParser(
        description="Employee Retirement Application. Use 'compute' to get retirement info or 'add' to add a new employee."
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Sub-commands")
    subparsers.add_parser("compute", help="Compute retirement information")

    add_parser = subparsers.add_parser("add", help="Add a new employee")
    add_parser.add_argument("--name", type=str, required=True, help="Name of the employee")
    add_parser.add_argument("--date_of_birth", type=str, required=True, help="Date of birth (YYYY-MM-DD)")
    add_parser.add_argument("--salary", type=float, required=True, help="Salary of the employee")

    args = parser.parse_args()

    logger.info("Starting Employee Retirement Application.")
    db = SessionLocal()
    try:
        employee_repository = EmployeeRepository(db)
        if args.command == "compute":
            compute_retirement_info(employee_repository)
        elif args.command == "add":
            add_new_employee(employee_repository, args)
        else:
            parser.print_help()
    finally:
        db.close()

if __name__ == "__main__":
    main()