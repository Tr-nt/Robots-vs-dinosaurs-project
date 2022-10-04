from weapon import weapon 
class robot:

    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = weapon()

    def attack (self, dinosaur):
        