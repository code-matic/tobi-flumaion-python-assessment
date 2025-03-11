import importlib
import sys
from unittest.mock import patch
from tests.conftest import FixedDateTime
from src import main


def test_main_compute(capsys, monkeypatch, mock_employees, employee_repository):
    """
    Test the main() script function.

    The fixed date is set to 2025-01-02 .
    Only "Goodness" to appear, with a total salary of 85000.
    """

    monkeypatch.setattr("src.scripts.employee.datetime", FixedDateTime)
    test_args = ["prog", "compute"]
    monkeypatch.setattr(sys, "argv", test_args)
    main.main()
    captured = capsys.readouterr().out

    print("captured", captured)
    # Assertions: verify that the printed output contains the expected information.
    assert "Computation Date: 2025-01-02" in captured
    assert "Retiring Employees:" in captured
    # Only "Goodness" should be included.
    assert "Goodness" in captured
    # Total salary liability should equal 85000 (Goodness' salary).
    assert "Total Salary Liability: 85000" in captured



def test_main_add(capsys, monkeypatch, employee_repository):
    """
    Test main() when run with the 'add' subcommand.
    
    Simulate adding a new employee with:
      - name: Samuel
      - date_of_birth: 1940-10-10
      - salary: 10000.0
    
    Expect that the output confirms the new employee's details.
    """

    # Simulate command-line arguments for the "add" subcommand.
    cli_args =  ["prog", "add", "--name", "Samuel", "--date_of_birth", "1940-10-10", "--salary", "10000.0"]
    monkeypatch.setattr(sys, "argv", cli_args )
    
    main.main()
    
    # Capture printed output.
    captured = capsys.readouterr().out
    print("Captured add output:", captured)  # Debug output (optional)
    
    # Assertions.
    assert "New employee added:" in captured
    assert "Samuel" in captured
    assert "datetime.date(1940, 10, 10)" in captured
    assert "10000" in captured or "10000.0" in captured