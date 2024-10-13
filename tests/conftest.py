import pytest


@pytest.fixture
def global_data():
    return [
        {
            "given_name": "Ehsan",
            "family_name": "Peymani",
            "title": "Driver",
        },
    ]