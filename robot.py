
from Weapon import weapon 
class robot:

    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = weapon("Sword", 30)

    def attack (self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} for {self.active_weapon.attack_power} damage!')
        print(f'dinosaur has {dinosaur.health} remaining')
