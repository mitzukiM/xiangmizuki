from typing import Callable


def master(func: Callable) -> Callable:
    def subordinate(*args, **kwargs):
        result = func(*args, **kwargs)  # must be here!!!!!!!!!!!!!!!
        if isinstance(result, int):
            return result + 10

        return result

    return subordinate  # no round brackets !!!!!!!!!!!!!!


@master
def foo(number: int) -> int:
    return number


res = foo(6)
print(res)
