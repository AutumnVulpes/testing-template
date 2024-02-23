import math
import os

def add(a, b) -> int:
    return math.floor(a + b)

def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endwith('.'):
        return s
    else:
        return s + '.'