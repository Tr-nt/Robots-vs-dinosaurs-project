class dinosaur:

    def __init__(self, name, attack_power) -> None:
        self.name = name 
        self.attack_power = attack_power
        self.health = 100

    def attack (self, robot):
        print(f"{self.name} attacked {robot.name} for {self.attack_power}")