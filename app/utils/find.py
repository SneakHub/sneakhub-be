from typing import Callable, List, TypeVar, Union

# create "template" T which will be specified later
# when the function is actually called and used
T = TypeVar("T")

# Type hint "Callable" indicates an 'callable object' (here is function fn)
# the function takes singles argument typed 'T', then response with 'boolean' value
def find(fn: Callable[[T], bool], arr: List[T]) -> Union[T, None]:
    for ele in arr:
        if fn(ele):
            return ele
    return None
