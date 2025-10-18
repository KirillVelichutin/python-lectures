import random
from enum import StrEnum
from threading import ExceptHookArgs
from typing import Self

class Names(StrEnum):
    JOHN = "John Lennon"
    PAUL = "Paul McCartney"
    GEORGE = "George Harrison"
    RINGO = "Ringo Starr"


class Beetle:
    health_points: int
    name: Names

    def __init__(
        self,
        health_points: int = 100,
        name: Names = Names.JOHN,
    ) -> None:
        self.health_points = health_points
        self.name = name

    def __eq__(self, other: Self) -> bool:
        return self.health_points == other.health_points

    def __lt__(self, other: Self) -> bool:
        return self.health_points < other.health_points

    def __le__(self, other: Self) -> bool:
        return self.health_points <= other.health_points

    def __str__(self) -> str:
        return f'Beetle(name="{self.name}", hp={self.health_points!r})'

    def styling(self) -> str:
        if self.name is Names.JOHN:
            return "in Johny style"
        elif self.name is Names.PAUL:
            return "in McCartney style"
        return "without style"

    def attack(self, other: Self) -> None:
        print(f"{self.name} attacking {other.name} {self.styling()}")
        other.health_points -= 10