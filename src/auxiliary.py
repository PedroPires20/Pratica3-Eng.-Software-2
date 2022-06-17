import math

def sign(a: int) -> int:
    return -1 if a < 0 else 1

def mdc(a: int, b: int) -> int:
    if not isinstance(a, int):       
        raise TypeError(f"Invalid type '{type(a)}' given for the MDC function!")
    if not isinstance(b, int):       
        raise TypeError(f"Invalid type '{type(b)}' given for the MDC function!")
    a = abs(a)
    b = abs(b)
    if a < b:
        temp = a
        a = b
        b = temp
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

