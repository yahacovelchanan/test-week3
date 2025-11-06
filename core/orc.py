import random
class Orc:
    def __init__(self,name,hp,type,speed,power,armor_rating,weapon):
        self.name="orc"
        self.hp=50
        self.type=Orc
        self.speed=random.randint(1,5)
        self.power=random.randint(10,15)
        self.armor_rating=random.randint(2,8)
        self.weapon=random.choice(["Axe","Sword","Knife"])
    def speek():
        print("Orc Bob is furious!")

    def attack(self):
        pass
        