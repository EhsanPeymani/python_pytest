from src.format_data import format_data_for_display, format_data_for_excel, connect
import pytest


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
        {
            "given_name": "",
            "family_name": "Khan",
            "title": "Project Manager",
        },
        {
            "given_name": "An",
            "family_name": "",
            "title": "Project Manager",
        },
    ]
    

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
        "Khan: Project Manager",
        "An: Project Manager",
    ]


def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
,Khan,Project Manager
An,,Project Manager
"""


def test_format_data_for_display_with_global_data(global_data):
    assert format_data_for_display(global_data) == [
        "Ehsan Peymani: Driver"
    ]
    

@pytest.mark.parametrize("input", [0, 1])
def test_connect(input):
    if input == 1:
        with pytest.raises(ConnectionError):
            connect(input)
    else:
        assert connect(input) == 1
        