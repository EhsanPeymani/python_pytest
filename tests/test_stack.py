from src.stack import Stack
import pytest

@pytest.fixture
def stack():
    return Stack()


def test_constructor(stack):
    assert isinstance(stack, Stack)
    assert len(stack) == 0


def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    
    stack.push(2)
    assert len(stack) == 2  
    
    
def test_pop(stack):
    stack.push(3)
    assert stack.pop() == 3
    

@pytest.mark.smoke
def test_pop_empty_stack():
    s = Stack()
    assert s.pop() == None 