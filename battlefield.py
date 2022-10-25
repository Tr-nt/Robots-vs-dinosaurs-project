from Robot import robot
from Dinosaur import dinosaur

class battlefield:
    
    def __init__(self) -> None:
        self.Robot = robot("Robo")
        self.Dinosaur = dinosaur("Dino", 20)

    
    def display_welcome(self):
        print ("Welcome to the game")

    def battle_phase(self):
        self.Robot.attack(self.Dinosaur)
        self.Dinosaur.attack(self.Robot)
    
    def display_winner(self):
        if self.Robot.health < 0:
            print(f'{self.Dinosaur.name} wins the fight')
        elif self.Dinosaur.health < 0:
            print(f'{self.Robot.name} wins the fight')
    
    def run_game(self):
        self.display_welcome()
        
        while self.Dinosaur.health > 0 and self.Robot.health > 0:
           self.battle_phase()
        
        self.display_winner()

        