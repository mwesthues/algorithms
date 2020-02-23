import numpy as np
import sys
import typing

def sqrt(value: float) -> float:
    if (value < 0):
        return np.nan
    
    err: float = 1e-15
    t: float = value
    while abs(t - value/t) > err * t:
        t = (value/t + t) / 2.0
    return t



if __name__ == '__main__':
    sys.exit(sqrt(sys.argv))
