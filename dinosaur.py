class dinosaur:

    def __init__(self, name, attack_power) -> None:
        self.name = name 
        self.attack_power = attack_power
        self.health = 100

    def attack (self, robot):
        robot.health -= self.attack_power 
        print(f"{self.name} attacked {robot.name} for {self.attack_power} damage!")
        print(f'robot has {robot.health} remaining')