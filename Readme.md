# QA Automation - API Testing

Automated API test suite using Python and pytest

## Tech Stack
- Python 3.10
- pytest
- request
- pytest-html

## Project Structure
tests/ #test file
utils/ #Helper function
run_test.py #Main test runner
pytest.ini #pytest configuration

# How To Run
1. Clone the repository
2. Create virtual environment  : 'python -m venv venv'
3. Activate : 'venv\Scripts\activate
4. Install dependencies: 'pip install -r requirements.txt'
5. Run test : 'python run_test.py'

# Test Coverage
- GET single user - status code validation
- GET single user - response field validation
- GET single user - data accuracy
- GET all user - list validation
- GET invalid user - error handling 

