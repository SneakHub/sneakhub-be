from typing import TypeVar, Callable, List, Union

# create "template" type T indicates that this type will be specified later
# when the function is actually called and used.
T = TypeVar("T")

# Callable indicates that function 'fn' takes a single argument typed T
# and response with value typed 'boolen'
def find(fn: Callable[[T], bool], arr: List[T]):
    for ele in arr:
        if fn(ele):
            return ele
    return None
