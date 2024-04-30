from typing import Callable, List, TypeVar

T = TypeVar("T")


def find(fn: Callable[[T], bool], arr: List[T]):
    for ele in arr:
        if fn(ele):
            return ele
    return None
