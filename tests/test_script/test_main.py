import pytest
from unittest.mock import patch
from tests.conftest import FixedDateTime
from src import main


def test_main(capsys, monkeypatch, mock_employees):
    """
    Test the main() script function.

    The fixed date is set to 2025-01-02 .
    Only "Goodness" to appear, with a total salary of 85000.
    """
    
    monkeypatch.setattr("src.repository.employee.EMPLOYEES_DB", mock_employees)
    monkeypatch.setattr(main, "datetime", FixedDateTime)
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
