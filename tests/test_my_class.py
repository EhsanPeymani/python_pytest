import pytest
from unittest.mock import patch, MagicMock
from src.my_class import MyClass

# method 1 
def test_my_method_using_patch_as_context_manager():
    with patch('src.my_class.MyClass.method_one') as mock_method:
        return_value = "mocked return value"
        mock_method.return_value = return_value
        
        my_class = MyClass()
        result = my_class.method_one()
        assert result == return_value
        mock_method.assert_called_once()


# method 2
@patch('src.my_class.MyClass.method_one', return_value="mocked return value")
def test_my_method_using_patch_as_decorator(mocked_method):
    my_class = MyClass()
    result = my_class.method_one()
    assert result == "mocked return value"        
    mocked_method.assert_called_once()


# method 3
@patch('src.my_class.MyClass.method_one', return_value="mocked return value 1")
@patch('src.my_class.MyClass.method_two', return_value="mocked return value 2")
def test_my_method_using_patch_as_decorator_multiple_methods(mocked_method_1, mocked_method_2):
    my_class = MyClass()
    assert my_class.method_one() == "mocked return value 1"
    assert my_class.method_two("my_name") == "mocked return value 2"
    mocked_method_1.assert_called_once()
    mocked_method_2.assert_called_once()
    
   
# methdo 4 
def test_my_method_using_magic_mock():
    my_class = MyClass()
    my_class.method_two = MagicMock(return_value="mocked response")
    
    assert my_class.method_two("my_name") == "mocked response"
    my_class.method_two.assert_called_once_with("my_name")
    print(f"call count: {my_class.method_two.call_args_list[0]}")
        
        
# method 5
@pytest.fixture
def mocked_method_2():
    my_class = MyClass()
    my_class.method_two = MagicMock(return_value="mocked response in fixture")
    return my_class


def test_my_method_using_magic_mock_in_fixture(mocked_method_2):
    assert mocked_method_2.method_two("my_name") == "mocked response in fixture"
    mocked_method_2.method_two.assert_called_once_with("my_name")
    

# method 6
@pytest.fixture
def mocked_method_2_by_patch():
    with patch('src.my_class.MyClass.method_two') as mock:
        mock.return_value = "mocked response in fixture and patch"
        yield mock


def test_my_method_using_patch_in_fixture(mocked_method_2_by_patch):
    my_class = MyClass()
    assert my_class.method_two("my_name") == "mocked response in fixture and patch"
    mocked_method_2_by_patch.assert_called_once_with("my_name")