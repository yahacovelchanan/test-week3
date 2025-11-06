import random

class Player:
    def __init__(self,name,hp=70,speed=90,power=98,armor_ratin,profession):
        self.name=name
        self.hp=50
        self.speed=random.randint(5,10)
        self.power=random.randint(5,10)
        self.armor_rating=random.randint(5,15)
        self.profession=random.choice(["fighter","doctor"])
        if self.profession== "fighter":
            self.power+=2
        if self.profession== "doctor" :
            self.hp+=10
              
             
    def speek(self):
        print(f"{self.name} is going to break your face.")

    def attack(self):
        self.value_per_queue=random.randint(1,20)
        self.value_per_queue+=self.speed
   
          
t1=Player("simi",50,6,9,8,"kil") 
print(t1.hp)          
            
            
        
        
        
        