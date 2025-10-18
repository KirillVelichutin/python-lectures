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


class BeetlesArmy:
    beetles_list: list[Beetle]
    beetles_name: Names
    beetles_max_health_points: int

    def __init__(
        self,
        beetles_name: Names,
        beetles_army_size: int = 20,
        beetles_max_health_points: int = 100,
    ):
        self.beetles_list = []
        self.beetles_name = beetles_name
        self.beetles_max_health_points = beetles_max_health_points

        for _ in range(beetles_army_size):
            beetle = Beetle(
                health_points=random.randint(1, self.beetles_max_health_points),
                name=self.beetles_name,
            )
            self.beetles_list.append(beetle)

    def __len__(self) -> int:
        return len(self.beetles_list)

    def __add__(self, other: Self) -> Self:
        if self.beetles_name != other.beetles_name:
            raise ValueError("Cannot make two different-named beetles friends")
        new_beetles_list: list[Beetle] = self.beetles_list + other.beetles_list
        new_army = self.__class__(
            beetles_army_size=1,
            beetles_name=self.beetles_name,
            beetles_max_health_points=self.beetles_max_health_points,
        )
        new_army.beetles_list = new_beetles_list
        return new_army

    def print_army_listing(self):
        for beetle in self.beetles_list:
            print(beetle)


if __name__ == "__main__":
    # m1 = Beetle(health_points=90, name=Names.JOHN)
    # m2 = Beetle(health_points=90, name=Names.PAUL)
    # print("==", m1 == m2)
    # print("!=", m1 != m2)
    # print("<", m1 < m2)
    # print(">", m1 > m2)
    # print("<=", m1 <= m2)
    # print(">=", m1 >= m2)

    # print(m1, str(m2))

    print("ARMY 1:")
    ba1 = BeetlesArmy(
        beetles_name=Names.PAUL,
        beetles_army_size=9,
        beetles_max_health_points=30,
    )
    ba1.print_army_listing()
    print()

    print("ARMY 2:")
    ba2 = BeetlesArmy(
        beetles_name=Names.JOHN,
        beetles_army_size=10,
        beetles_max_health_points=100,
    )
    ba2.print_army_listing()
    print()

    # # LBYL
    # if ba1.beetles_name == ba2.beetles_name:
    #     ba3 = ba1 + ba2
    #     print("ARMY 3:")
    #     ba3.print_army_listing()
    #     del ba1, ba2
    # else:
    #     print("You stooopid")

    # EAFP
    try:
        ba3 = ba1 + ba2
        print("ARMY 3:")
        ba3.print_army_listing()
        del ba1, ba2
    except ValueError as ex:
        print(f"You stooopid: {ex}")
    except TypeError as ex:
        print("Typing is stoopid")

# Задание:
#
# Продолжить логику битв армий жуков
# Где каждая армия бьёт другую по очереди
# пока у неё не закончатся жуки
#
# Жук умирает при здоровье <= 0
# Жук получает +10 хп за убийство жука, но не больше своего max_hp в армии
#
# Весь прогресс битвы можно красиво выводить с помощью rich
#
# Должен быть функционал сравнения армий
#
# Все данные о битве (сколько армий и под каким именем) - запрашивайте у пользователя
# Урон должен быть определен так же как и ХП, но при .attack() варьироваться каждый раз от рандома