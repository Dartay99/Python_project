from dataclasses import dataclass

from actors.actor import Actor

@dataclass

class Warrior(Actor): #Базовый класс для тех кто может атаковать 
    attack_point: int
    
    # def __init__(self):
    #   raise NotImplementedError("Warrior is an abstract class")
    
    def is_alive(self):
        return self.hp>0
    
    def attack(self, enemy):
        enemy.hp -= self.attack_point
        print(f"{self.first_name} attacked {enemy.first_name} with {self.attack_point} attack points")
        print(f"{enemy.first_name} has {enemy.hp} health points left")