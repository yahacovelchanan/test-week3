import random
class Goblin:
    def __init__(self,name,hp,type,speed,power,armor_rating,weapon):
        self.name="goblin"
        self.hp=20
        self.type=Goblin
        self.speed=random.randint(1,5)
        self.power=random.randint(1,5)
        self.armor_rating=1
        self.weapon=random.choice(["Axe","Sword","Knife"])
    def speek():
        print("Goblin Joe is furious!")

    def attack(self):
        