from typing import List, Tuple


def _head_tail(lst: List) -> Tuple:
    return ([lst[0]], lst[1:])

def head(lst: List) -> List:
    if len(lst) > 1:
        return _head_tail(lst)[0]
    else:
        return lst

def tail(lst: List) -> List:
    if len(lst) > 1:
        return _head_tail(lst)[1]
    else:
        return lst
    
def reverse(lst: List) -> List:
    if len(lst) > 1:
        return reverse(tail(lst)) + head(lst)
    else:
        return lst