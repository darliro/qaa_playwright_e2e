[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-black.svg)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-green?logo=playwright)](https://playwright.dev/)
[![Allure TestOps](https://img.shields.io/badge/Allure-blueviolet?logo=allure)](https://docs.qameta.io/allure-testops/)

## E2E Test Automation Project for HRM System
### by DarliRo
This project is for writing and running automated tests using **Pytest** & **Playwright** (TBD)

### Initial Setup
- [ ] Install [Python](https://www.python.org/downloads/) (version 3.12 or later)
- [ ] Install [PDM](https://pdm-project.org/latest/#recommended-installation-method) for dependency management
- [ ] Create and activate a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
- [ ] Install project dependencies: `pdm lock && pdm sync`
- [ ] Set up pre-commit hooks (auto-code check before commit): `pre-commit install -f`
- [ ] Create a `.env` file to store and retrieve environment variables: `touch .env`

### Running Tests Locally
#### Through Terminal:
- Run the test: `pytest -s -v tests/path_to_file_or_directory`
- Add the following to the command to generate a report (json files): `--alluredir=allure-results`

#### Through IDE:
- Check in the interpreter settings that the `.venv` virtual environment of the project is selected
- Run tests using the "**run**" button or play icon, depending on your IDE

### Running Tests in GitHub Actions
#### Manual Run:
- Access the [GitHub Actions page](https://github.com/darliro/QAAPractice/actions)
- Click the **Run workflow** button on the relevant workflow
- Click **Run workflow** again

### Allure Report Setup
- Install [Allure Report](https://docs.qameta.io/allure/#_installing_a_commandline)
- Generate a report based on the latest test run: `allure generate allure-results --clean -o allure-report`
- Open the report in a browser: `allure open allure-report`

### Code Linting and Formatting with [ruff](https://github.com/astral-sh/ruff)
- Run the linter to check code for errors: `ruff check path_to_file_or_folder` (with autofix: add `--fix`, for the entire project: add `.` at the end)
- Run the formatter to standardize code style: `ruff format path_to_file_or_folder` (with autofix: add `--fix`, for the entire project: add `.`)

`Tip:`
At each level of the `tests` folder, you can have a `conftest.py` with fixtures or hooks specific to that level of tests.
