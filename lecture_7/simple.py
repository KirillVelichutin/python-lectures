class Human:
    name: str
    legs: int
    eyes: int
    hands: int
    hair_color: str
    
    def __init__(
        self, 
        name: str = "Vova", 
        legs: int = 2,
        eyes: int = 2,
        hands: int = 2,
        hair_color: str = "brown"
        ):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.hands = hands
        self.Hair_color = hair_color
    
    def blink(self):
        name = "Andrey"
        print(f"{self.name} blinked with {self.eyes} eyes")
    
    def walk(self):
        print(f"{self.name} walked away")
    
    def break_plank(self, plank_material: str = "wooden", quantity: int = 2):
        print(f"{self.name} broke {quantity} {plank_material} planks")
        
        
class SmartHuman(Human):
    glasses: bool
    IQ: int
    
    def __init__(self, glasses: bool = True, IQ: int = 130):
        super().__init__()
        self.glasses = glasses
        self.IQ = IQ
        
    
    def blink(self):
        print(f"Smart {self.name} blinked with {self.eyes} eyes "
              f"and with glasses {'on' if self.glasses is True else 'off'}")

if __name__ == '__main__':
    human1 = Human()
    
    human1.blink()
    human1.break_plank()
    human1.break_plank(plank_material = "plastic", quantity = 3)
    
    smart_human1 = SmartHuman()
    smart_human1.blink()