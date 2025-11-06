from core import goblin,player,orc 
import random

def create_player():
        player1=player.Player(name=str(input("Enter your name.")))
        return player1

def choose_random_monster():
    monster1=random.choice[goblin.Goblin(),orc.Orc()]
    return monster1

def start():
        print("""Hello to the terrible monster game""")
        
def show_menu():
        battle=1
        exit=2
        user=int(input("""
              If you want to play press 1
              If you want to exit press 2
              """))
        return user        
    
def battle(player, monster):
    while player!=0 or monster!=0:
        start_game=random.randint(1,6)
def show_menu():
        battle=1
        exit=2
        user=int(input("""
              If you want to play press 1
              If you want to exit press 2
              """))
        return user       
        
       