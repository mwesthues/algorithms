from fundamentals.counter import Counter
import numpy as np
from typing import List

class Flips():
    def __init__(self) -> None:
        pass

    def flip(self, times: int):
        heads = Counter("heads")
        tails = Counter("tails")

        throws: List[int] = [np.random.binomial(1, p=0.5) for x in range(times)]
        [heads.increment() for throw in throws if throw == 0]
        [tails.increment() for throw in throws if throw == 1]
        delta: int = abs(heads.tally() - tails.tally())
        print("heads: {}".format(heads.tally()))
        print("tails: {}".format(tails.tally()))
        print("delta: {}".format(delta))

