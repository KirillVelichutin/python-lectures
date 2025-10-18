from abc import abstractmethod
from typing import override

class BaseDuck:
    wings: int = 2
    beak: bool = True
    
class BaseToy:
    material: str = 'plastic'
        
class MixinWalkable:
    legs: int = 2
    def walk(self):
        print(f"Walked away on {self.legs} feets")

class MixinNoisable:
    @abstractmethod
    @override
    def make_noise(self, volume_db: int) -> None:
        raise NotImplementedError

class MixinDustable:
    def get_dusty(self) -> None:
        print('gets dusty')

class Duckess(BaseDuck, MixinNoisable, MixinWalkable, MixinDustable):
    def make_noise(self, volume_db: int) -> None:
        print(f'quackie ({volume_db} dB)')

class Duck(BaseDuck, MixinNoisable, MixinWalkable, MixinDustable):
    def make_noise(self, volume_db: int) -> None:
        print(f'quack ({volume_db} dB)')

class ToyDuck(BaseDuck, BaseToy, MixinDustable):
    pass

if __name__ == "__main__":
    d1 = Duck()
    d1.make_noise(12)
    d1.walk()
    
    ds1 = Duckess()
    ds1.make_noise(12)
    
    td1 = ToyDuck()
    td1.get_dusty()