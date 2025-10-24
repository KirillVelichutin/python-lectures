import random
from enum import StrEnum
from threading import ExceptHookArgs
from typing import Self
from rich import print as rprint


class Names(StrEnum):
    JOHN = f"[yellow]John Lennon[/yellow]"
    PAUL = f"[green]Paul McCartney[/green]"
    GEORGE = f"[red]George Harrison[/red]"
    RINGO = f"[blue]Ringo Starr[/blue]"
    
    
class Beetle:
    health_points: int
    name: Names
    max_power: int
    def __init__(
        self,
        health_points: int = 100,
        name: Names = Names.JOHN,
        max_power: int = 10
    ) -> None:
        self.health_points = health_points
        self.name = name
        self.max_power = max_power
    def __eq__(self, other: Self) -> bool:
        return self.health_points == other.health_points
    def __lt__(self, other: Self) -> bool:
        return self.health_points < other.health_points
    def __le__(self, other: Self) -> bool:
        return self.health_points <= other.health_points
    def __str__(self) -> str:
        return f'Beetle(name="{self.name}", hp={self.health_points!r}, power={self.max_power!r})'
    def styling(self) -> str:
        if self.name is Names.JOHN:
            return "in [yellow italic]Johny[/yellow italic] style"
        elif self.name is Names.PAUL:
            return "in [green italic]McCartney style[/green italic]"
        return "[italic]without[/italic] style"
    def attack(self, other: Self) -> None:
        attack_power = random.randint(1, self.max_power)
        rprint(f"{self.name} attacking {other.name} {self.styling()} with {attack_power} damage")
        other.health_points -= attack_power


class BeetlesArmy:
    beetles_list: list[Beetle]
    beetles_name: Names
    beetles_max_health_points: int
    beetles_max_power: int
    def __init__(
        self,
        beetles_name: Names,
        beetles_army_size: int = 20,
        beetles_max_health_points: int = 100,
        beetles_max_power: int = 10
    ):
        self.beetles_list = []
        self.beetles_name = beetles_name
        self.beetles_max_health_points = beetles_max_health_points
        self.beetles_max_power = beetles_max_power
        for _ in range(beetles_army_size):
            beetle = Beetle(
                health_points=random.randint(1, self.beetles_max_health_points),
                name=self.beetles_name,
                max_power= self.beetles_max_power,
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
            beettles_max_power = self.beetles_max_power
        )
        new_army.beetles_list = new_beetles_list
        return new_army
    def rprint_army_listing(self):
        for beetle in self.beetles_list:
            rprint(beetle)


def start():
    rprint("I see, you are thirst for the blodd.")
    rprint("Well, input the number of armies which you're willing to crush: ")
    user_army_size = int(input())
    rprint(user_army_size)

    if user_army_size > 4:
        rprint("You are maniac! We don't even have such quantity of beetles. Go away, psycho!")
    elif user_army_size == 0:
        rprint("You are pacifist! Go away to your unicorn land.")
    elif user_army_size == 1:
        rprint("There is safety in numbers")
    elif user_army_size < 0:
        rprint("What do you even want to see with such requirenments? Dead beetles don't fight.")
    else:
        initiate_armies(user_army_size)
        
        
def initiate_armies(user_army_size):
    armies_names = []
    while len(armies_names) < user_army_size:
        rprint(f"How army {len(armies_names) + 1} will be called ([yellow]JOHN[/yellow], [green]PAUL[/green], [red]GEORGE[/red], [blue]RINGO[/blue])?: ")
        
        army_name = input()
        rprint(army_name)
        
        if army_name.upper() != "JOHN" and army_name.upper() != "PAUL" and army_name.upper() != "GEORGE" and army_name.upper() != "RINGO":
                
            rprint("There are no beetles with this name. Try again")
            
        else:
            armies_names.append(army_name)
            
            
    armies = []
    for i, army_name in enumerate(armies_names):
        name_enum = Names[army_name.upper()]
        rprint(f"Input the quantity of beetles in army {i + 1}: ")
        army_size = int(input())
        rprint(army_size)
        
        rprint(f"Input the max health value of beetles in army {i + 1}: ")
        max_health_points = int(input())
        rprint(max_health_points)
        
        rprint(f"Input the max power value of beetles in army {i + 1}: ")
        max_power = int(input())
        rprint(max_power)
        
        army = BeetlesArmy(
            beetles_name = name_enum,
            beetles_army_size = army_size,
            beetles_max_health_points = max_health_points,
            beetles_max_power = max_power
        )
        
        armies.append(army)
        
    rprint(f"\nOverall {len(armies)} armies were created for the great battle!")
    
    rprint("Start the battle?")
    decision = input()
    rprint(decision)
    
    if decision.upper() == "YES":
        battle(armies)
    else:
        rprint("The gates of Valhalla are closed for you forever.")
    

def battle(armies):    
    while len(armies) > 1:
        ba1 = armies[0]
        ba2 = armies[1]
        
        if len(ba1) !=0 and len(ba2) != 0:
            ba1.beetles_list[0].attack(ba2.beetles_list[0])
            if ba2.beetles_list[0].health_points <= 0:
                rprint(f"{ba2.beetles_list[0].name} is dead")
                ba2.beetles_list.pop(0)
                if (ba1.beetles_list[0].health_points + 10) <= ba1.beetles_max_health_points:
                    ba1.beetles_list[0].health_points += 10
            if len(ba2) != 0:
                ba2.beetles_list[0].attack(ba1.beetles_list[0])
                if ba1.beetles_list[0].health_points <= 0:
                    rprint(f"{ba1.beetles_list[0].name} is [bold italic]dead[/bold italic]")
                    ba1.beetles_list.pop(0)
                    if (ba2.beetles_list[0].health_points + 10) <= ba1.beetles_max_health_points:
                        ba2.beetles_list[0].health_points += 10
            rprint(f"\n{ba1.beetles_name} army: {len(ba1)} beetles left", f"{ba2.beetles_name} army: {len(ba2)} beetles left", "-" * 20, sep="\n")
            
        else:
            if len(ba1) == 0:
                rprint("X" * 40, f"{ba1.beetles_name} army is [bold italic]dead[/bold italic]", "X" * 40, sep="\n")
                armies.pop(0)
            else:
                rprint(f"{ba2.beetles_name} army is [bold]dead[/bold]")
                armies.pop(1)
                
    rprint("*" * 40, f"{armies[0].beetles_name} army is a [bold]winner[/bold]!", "*" * 40, sep="\n")            
        
        
        
if __name__ == "__main__":
    start()