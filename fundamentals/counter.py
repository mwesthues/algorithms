import typing

class Counter():
    def __init__(self, name: str) -> None:
        self.name = name
        self.count: int = 0
    
    def increment(self) -> None:
        self.count += 1

    def tally(self) -> int:
        return self.count

