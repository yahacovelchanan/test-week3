import random
from core import goblin,orc
     
class Player:
    def __init__(self,name,munster=random.choice[goblin.Goblin(),orc.Orc()],hp=50,speed=random.randint(5,10),power=random.randint(5,10),armor_rating=random.randint(5,15),profession=random.choice(["fighter","doctor"])):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.speed=speed
        self.power=power
        self.armor_rating=armor_rating
        self.profession=profession
        self.munster=munster
        if self.profession== "fighter":
            self.power+=2
        if self.profession== "doctor" :
            self.hp+=10
              
             
    def speek(self):
        print(f"{self.name} is going to break your face.")

    def attack(self):
        self.value_per_queue=random.randint(1,20)
        self.value_per_queue+=self.speed
        return self.value_per_queue
    
    def results_of_the_impact(self):
        if self.value_per_queue>self.munster.armor_rating:
            injury=random.randint(1,6)
            injury+=self.power
            self.munster.hp-=injury
            if self.munster.hp<=0:
                print(f"{self.munster}Life is over.")
        else:
            print("miss")        
            
            
    
  
        
   
        
          
            


        
   
          

            
        
        
        
        