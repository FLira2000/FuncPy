from functools import wraps
from typing import Generator, List, Tuple

def _type_guard(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        if any([type(n) == type( tuple() ) or type(n) == type( set() ) or type(n) == range for n in args]):
            raise Exception('Those functions are suposed to be used with Lists only. ')
        return callback(*args, **kwargs)
    return wrapper

@_type_guard
def _head_tail(lst: List) -> Tuple:
    return ([lst[0]], lst[1:])

@_type_guard
def head(lst: List) -> List:
    if len(lst) > 1:
        return _head_tail(lst)[0]
    else:
        return lst

@_type_guard
def tail(lst: List) -> List:
    if len(lst) > 1:
        return _head_tail(lst)[1]
    else:
        return lst

@_type_guard    
def reverse(lst: List) -> List:
    if len(lst) > 1:
        return reverse(tail(lst)) + head(lst)
    else:
        return lst

@_type_guard
def take(n: int, lst: List) -> List:
    if n > len(lst):
        return lst
    if n == 1:
        return head(lst)
    return head(lst) + take(n-1, tail(lst))

def generator(fn, start = 0, end = None) -> Generator:
    if end != None and fn(start) > end:
        return fn(start)
    yield fn(start)
    yield from generator(fn, fn(start), end)
