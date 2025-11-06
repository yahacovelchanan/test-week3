import random
from core import player
class Orc:
    def __init__(self,type:Orc,player:player.Player,name="orc",hp=50,speed=random.randint(1,5),power=random.randint(10,15),armor_rating=random.randint(2,8),weapon=random.choice(["Axe","Sword","Knife"])):
        self.name=name
        self.hp=hp
        self.player=player
        self.type=type
        self.speed=speed
        self.power=power
        self.armor_rating=armor_rating
        self.weapon=weapon
    def speek():
        print("Orc Bob is furious!")

    def attack(self):
        self.value_per_queue=random.randint(1,20)
        self.value_per_queue+=self.speed
        return self.value_per_queue
    
    def results_of_the_impact(self):
        if self.value_per_queue>self.player.armor_rating:
            injury=random.randint(1,6)
            if self.weapon=="Sword":
                self.power*=1
            if self.weapon=="Knife":
                self.power*=0.5
            if self.weapon=="Axe":
                self.power*=1.5        
            injury+=self.power    
            self.munster.hp-=injury
            if self.player.hp<=0:
                print(f"{self.player}Life is over.")
        else:
            print("miss") 
           