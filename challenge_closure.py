import typing
from typing import Callable as callable


def make_division_by(n: int) -> callable[[float], float]:
    """This closure returns a function that returns the division of an x number by n

    Args:
        n (int): any number positive integer
    """
    assert (isinstance(n, int) == True) and (
        n >= 1), "Your number need to be positive integer"
    #assert isinstance(n, int)
    assert n != 0, "You cannot divide by zero"

    def division(x: int) -> float:
        return x/n
    return division


def run() -> None:
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()
