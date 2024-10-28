[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-black.svg)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-green?logo=playwright)](https://playwright.dev/)
[![Allure TestOps](https://img.shields.io/badge/Allure-blueviolet?logo=allure)](https://docs.qameta.io/allure-testops/)

## E2E Test Automation Project for HRM System
### by DarliRo
This project is for writing and running automated tests using **Pytest** & **Playwright** (TBD)

### Initial Setup
- [ ] Install [Python](https://www.python.org/downloads/) (version 3.13+)
- [ ] Install [PDM](https://pdm-project.org/latest/#recommended-installation-method) for dependency management
- [ ] Create and activate a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
- [ ] Install project dependencies: `pdm lock && pdm sync`
- [ ] Set up pre-commit hooks (auto-code check before commit): `pre-commit install -f`
- [ ] Create a `.env` file to store and retrieve environment variables: `touch .env`

### Running Tests Locally
#### Through Terminal:
- Basic Run: `pytest -sv tests/path_to_file_or_directory`
- Run with Browser UI / Headed: `pytest -sv --headed tests/path_to_file_or_directory`
- Run with Slow Interactions / Debug:`pytest -sv --headed --slowmo 500 tests/path_to_file_or_directory`
- Generate Allure Reports: `pytest -sv --alluredir=allure-results tests/path_to_file_or_directory`

### Running Tests in GitHub Actions
#### Manual Run:
- Go to [GitHub Actions page](https://github.com/darliro/QAAPractice/actions)
- Find the desired workflow (e.g., UI Tests)
- Click the **Run workflow** button
- Select the branch you want to run
- Click **Run workflow** again to trigger the execution

### Allure Report Setup
- Install [Allure Report](https://docs.qameta.io/allure/#_installing_a_commandline)
- Generate a report based on the latest test run: `allure generate allure-results --clean -o allure-report`
- Open the report locally: `allure open allure-report`

### Code Linting and Formatting with [ruff](https://github.com/astral-sh/ruff)
- Check Code Quality: `ruff check path_to_file_or_folder`
- Autofix Errors: `ruff check path_to_file_or_folder --fix`
- Format Code: `ruff format path_to_file_or_folder --fix`

`Tips:`
- Usage of `conftest.py`:
At each level of the tests folder, you can place a `conftest.py` with fixtures or hooks specific to that level of testing
- Simulating **Debug Runs**:
Use `--headed` and `--slowmo` options to visually debug tests with browser UI and control interaction speeds
