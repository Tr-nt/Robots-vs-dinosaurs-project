from weapon import weapon 
class robot:

    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = weapon("Sword", 30)

    def attack (self, dinosaur):
        active_attack = self.active_weapon.attack_power
        print(f'{robot.name} attacked {dinosaur.name} for {active_attack} damage!')
