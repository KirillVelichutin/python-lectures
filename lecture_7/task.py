# Cоздать BaseCharacter, BaseInAnctionCaracter, BaseFunkoPop, BaseCosplayer, BaseHuman составить из них и из 
# Mixin...able логику наследований так, чтобы было минимум 6+ Mixin'ов (созданных, а не у каждого класса) с помощью 
# этих интерфейсов (миксинов) и наследования создать: Shrek, PussInBoots, Donkey, JackHorner
# на каждого должен быть и персонаж, и фанко поп, и косплеер
# итого должно быть: BaseCharacter: Shrek PussInBoots Donkey JackHorner
# BaseCharacter -> BaseInActionCharacter: Shrek -> ShrekInAction PussInBoots -> PussInBootsInAction Donkey -> DonkeyInAction JackHorner -> JackHornerInAction
# BaseCharacter -> BaseFunkoPop: Shrek -> ShrekInAction PussInBoots -> PussInBootsInAction Donkey -> DonkeyInAction JackHorner -> JackHornerInAction
# BaseCharacter -> BaseCosplayer <- BaseHuman: Shrek -> ShrekCosplayer PussInBoots -> PussInBootsCosplayer Donkey -> DonkeyCosplayer JackHorner -> JackHornerCosplayer
# [схема на GitVerse]

from rich import print as rprint


class MixinActionable:
    def perform_action(self):
        rprint(f"{self.name} показывает действие" if self.is_animated is True else f"{self.name} не может показывать действий")

class MixinCollectible:
    is_collectible: bool
    
    def __init__(self):
        self.is_collectible = True #default

class MixinCostumeWearable:
    costume: str
    
class MixinPoseable:
    def pose(self):
        rprint(f"*Косплеер в костюме '{self.costume}' делает сальто*")

class MixinAnimated:
    is_animated: bool

class MixinSpeakable:
    def speak(self):
        rprint(f"[bold]{self.name}:[/bold] [italic]{self.speech}")


class BaseHuman:
    is_human: bool



class BaseCharacter(MixinSpeakable, MixinAnimated):
    name: str
    is_animated: bool

class BaseInAcionCharacter(MixinActionable):
    pass

class BaseFunkoPop(MixinCollectible):
    
    def display(self):
        rprint(f"Вы только посмотрите! Это же - {self.name}!" if self.is_collectible is True else f"{self.name} - это кто? У нас такого нет")

class BaseCosplayer(BaseHuman, MixinPoseable, MixinCostumeWearable):
    def __init__(self):
        super().__init__()
        self.is_human = True



class Shrek(BaseCharacter):
    def __init__(self):
        self.name = f"[green]Шрек[/green]"
        self.is_animated = True
        self.speech = "Слушайте, сказочные твари! Не будьте как дома, вам тут официально не рады. Это факт."

class Donkey(BaseCharacter):
    def __init__(self):
        self.name = f"[red]Осёл[/red]"
        self.is_animated = True
        self.speech = "Не шевелиться! Мой дракон на боевом взводе. Я - отчаянный осёл!"
        
class PussInBoots(BaseCharacter):
    def __init__(self):
        self.name = f"[yellow]Кот в сапогах[/yellow]"
        self.is_animated = True
        self.speech = "Осёл... побежал. Но далеко ли можно убежать по покрытой маслом тарелке, да ещё в розовой пачке! И в сомбреро! И в лифчике из кокоса!"

class JackHorner(BaseCharacter):
    def __init__(self):
        self.name = f"[blue]Джэк Хорнен[/blue]"
        self.is_animated = True
        self.speech = "Пирог не приготовишь без дюжины смертей..."
        


class ShrekInAction(Shrek, BaseInAcionCharacter):
    pass

class DonkeyInAction(Donkey, BaseInAcionCharacter):
    pass

class PussInBootsInAction(PussInBoots, BaseInAcionCharacter):
    pass

class JackHornerInAction(JackHorner, BaseInAcionCharacter):
    pass

class ShrekFunkoPop(Shrek, BaseFunkoPop):
    pass

class DonkeyFunkoPop(Donkey, BaseFunkoPop):
    pass

class PussInBootsFunkoPop(PussInBoots, BaseFunkoPop):
    pass

class JackHornerFunkoPop(JackHorner, BaseFunkoPop):
    def __init__(self):
        super().__init__()
        self.is_collectible = False


class ShrekCosplayer(Shrek, BaseCosplayer):
    def __init__(self):
        super().__init__()
        self.costume = self.name

class DonkeyCosplayer(Donkey, BaseCosplayer):
    def __init__(self):
        super().__init__()
        self.costume = self.name

class PussInBootsCosplayer(PussInBoots, BaseCosplayer):
    def __init__(self):
        super().__init__()
        self.costume = self.name

class JackHornerCosplayer(JackHorner, BaseCosplayer):
    def __init__(self):
        super().__init__()
        self.costume = self.name
    
if __name__ == "__main__":
    s = Shrek()
    s.speak()
    
    d = Donkey()
    d.speak()
    
    pib = PussInBoots()
    pib.speak()
    
    jh = JackHorner()
    jh.speak()
    
    print("-" * 15)
    
    sin = DonkeyInAction()
    sin.perform_action()
    
    jhfp = JackHornerFunkoPop()
    jhfp.display()
    
    sc = ShrekCosplayer()
    sc.pose()