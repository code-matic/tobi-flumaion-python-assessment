from pydantic import BeforeValidator, AnyUrl
from typing import Annotated, Any


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings:
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = ["*"]
    PROJECT_NAME: str = "Retire Calc API"
    PROJECT_DESCRIPTION: str = '''
Problem Statement

	•	A company has [X]  number of employees.
	•	HR needs to calculate the number of employees retiring in a given year (assume retirement age to be on completion of 67).
	•	HR runs these computations twice a year - in June and December.


Design the following

	•	The ability to list employees retiring at the time the computation is run
	•	The total salary for those list of employees retiring (to calculate defined benefit liability)'''


settings = Settings()