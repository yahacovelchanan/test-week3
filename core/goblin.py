import random
from core import player
class Goblin:
    def __init__(self,type:Goblin,player:player.Player,name="goblin",hp=20,speed=random.randint(1,5),power=random.randint(1,5),armor_rating=1,weapon=random.choice(["Axe","Sword","Knife"])):
        self.name=name
        self.player=player
        self.hp=hp
        self.type=type
        self.speed=speed
        self.power=power
        self.armor_rating=armor_rating
        self.weapon=weapon
    def speek():
        print("Goblin Joe is furious!")

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
            self.player.hp-=injury
            if self.player.hp<=0:
                print(f"{self.player}Life is over.")
        else:
            print("miss") 
        