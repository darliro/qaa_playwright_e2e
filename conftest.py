import pytest
from faker import Faker
from datetime import datetime

faker = Faker()

DATA_GENERATORS = {
    "first_name": lambda: faker.unique.first_name(),
    "last_name": lambda: faker.unique.last_name(),
    "middle_name": lambda: faker.name_nonbinary(),
    "id": lambda: faker.unique.bothify(text="??????????"),
    "date": lambda: datetime.now().strftime("%Y-%d-%m"),
    "nationality": lambda: "Afghan",
    "marital_status": lambda: "Single",
}


@pytest.fixture(scope="function")
def data_generator():
    """
    Universal factory to generate different types of test data.
    """

    def _generate(data_type: str) -> str:
        if data_type not in DATA_GENERATORS:
            raise ValueError(f"Unknown data type: {data_type}")
        return DATA_GENERATORS[data_type]()

    return _generate
