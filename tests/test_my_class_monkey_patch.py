import pytest
from src.my_class import MyClass


@pytest.fixture
def mock_method_one(monkeypatch):
    monkeypatch.setattr(MyClass, "method_one", lambda self: "mocked by monkey patch for method one")


def test_method_two_monkeypatch(monkeypatch):
    monkeypatch.setattr(MyClass, "method_two", lambda self, name: "monekypatch return")
    
    my_class = MyClass()
    assert my_class.method_two("ehsan") == "monekypatch return"


def test_method_one_monkey_patch(mock_method_one):
    my_class = MyClass()
    assert my_class.method_one() == "mocked by monkey patch for method one"
