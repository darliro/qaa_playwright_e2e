import pytest
from faker import Faker


@pytest.fixture(scope="function")
def random_first_name() -> str:
    """
    Fixture to generate a random first name.
    """
    return Faker().first_name()


@pytest.fixture(scope="function")
def random_last_name() -> str:
    """
    Fixture to generate a random last name.
    """
    return Faker().last_name()


@pytest.fixture(scope="function")
def random_middle_name() -> str:
    """
    Fixture to generate a random middle name.
    """
    return Faker().name_nonbinary()


@pytest.fixture(scope="function")
def random_id() -> str:
    """
    Fixture to generate a random ID with a maximum of 10 characters.
    """
    return Faker().bothify(text="??????????")
