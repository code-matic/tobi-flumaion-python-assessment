## Employee Retirement Calculation Service
This project is designed to calculate the retirement of employees based on their date of birth and a defined retirement age (67 years). It provides two entry points:

- API Endpoint: A production-ready FastAPI application exposing endpoints for retrieving retiring employees and calculating total salary liability.
- Script Entry Point: A command-line script that computes and prints the list of retiring employees along with their total salary liability.

### Features
#### Modular Architecture:

- Models & Schemas: Employee models defined with Pydantic.
- Repository Layer: Abstracts data access via interfaces and concrete implementations.
- Services: Business logic for retirement computations.
- API & CLI Interfaces: Exposes functionality via a FastAPI REST API and a CLI script.
#### Dependency Injection:
Uses FastAPI’s dependency injection system to easily swap implementations (e.g., for testing or switching data sources).

#### Testing:
Comprehensive tests are provided using pytest with dependency overrides (via monkeypatch and patch).

#### Dockerized:
Dockerfiles for both API and script entry points.

### Tech Stack
- Language: Python 3.13
- Frameworks: FastAPI, Uvicorn
- Dependency Management: Poetry
- Testing: pytest, unittest.mock
- Containerization: Docker



### Installation
1. Clone the repository:

```bash Copy Edit

git clone git@github.com:code-matic/tobi-flumaion-python-assessment.git
cd employee-retirement-calculation
```

Install dependencies using Poetry:

```bash Copy Edit
poetry install
```

#### Running the Application
#### CLI Script
To run the script entry point locally:

```bash Copy Edit
poetry run python -m src.main
```
This will execute the main script and print the computation results to the console.

#### API Server
To run the FastAPI application locally with auto-reload (development mode):

```bash Copy Edit
poetry run uvicorn src.app:app --reload
```
Then, visit http://localhost:8000 to interact with the API.

### Running Tests
Tests are written using pytest. To run all tests, use:

```bash Copy Edit
poetry run pytest 
```

### Docker
The project includes two Dockerfiles for production:

#### API Docker Image
Dockerfile.api

Build the API image:

```bash Copy Edit
docker build -f Dockerfile.api -t employee-retirement-api .
```
Run the container:
    
```bash Copy Edit
docker run -p 8000:8000 employee-retirement-api
```
Your FastAPI application will be available at http://localhost:8000.

#### Script Docker Image
Dockerfile.script

Build the script image:
    
```bash Copy Edit
docker build -f Dockerfile.script -t employee-retirement-script .
```
Run the container:

```bash Copy Edit
docker run employee-retirement-script
```
This will run the CLI script and output the retirement computation results to the container logs.

#### Logging
The application uses Python's built-in logging module. A centralized logger is configured in src/utils/logger.py and used to provide clear, structured logs.

