import pytest


@pytest.fixture
def global_data(autouse=False):
    return [
        {
            "given_name": "Ehsan",
            "family_name": "Peymani",
            "title": "Driver",
        },
    ]
