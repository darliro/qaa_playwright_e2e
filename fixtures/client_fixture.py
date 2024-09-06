import pytest
from faker import Faker


@pytest.fixture(scope="function")
def random_first_name() -> str:
    """
    Fixture to generate a random first name.
    """
    return Faker().first_name()
