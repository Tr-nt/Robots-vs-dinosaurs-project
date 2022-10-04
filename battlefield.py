from robot import robot
from dinosaur import dinosaur

class battlefield:
    
    def __init__(self) -> None:
        dino = dinosaur("Dyno", 20)
        robo = robot("zoid")

    def run_game(self):
        while self.dino.health > 0 and self.robo.health > 0:
            pass

    def display_welcome(self):
        print ("Welcome to the game")

    def battle_phase(self):
        attack_1 = robot.attack
        attack_2 = dinosaur.attack

    def display_winner(self):
        pass 