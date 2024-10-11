from typing import List


class Stack:
    def __init__(self):
        self._storage: List = []
        self._val = 5

    def __len__(self):
        return len(self._storage)

    def push(self, value: float):
        self._storage.append(value)

    def pop(self) -> float:
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Value cannot be zero")
    return num1 / num2


def divide2(num1, num2):
    return num1 / num2
