from termcolor import colored
from utils import choices_to_str

choices = ["explore", "fight", "rest","trade","find_clues" , "find_food"]
inventory = []
health = 100
clues = 0 

done = False

while done  == False : 
    prompt = choices_to_str(choices)
    action = input(prompt + " >>> ")
    
    if action == "explore":
        print(colored("you explore the surrrondings and find an old map","yellow"))
        inventory.append("map")
    elif action == "fight":
        print(colored("you encounter a wild beast and fight bravely!","blue"))
        health -= 20
        if health <= 0:
            print(colored("you have been defeated.You adventure ends","red"))
            done = True
        else :
            print(colored("great battle!!!"))
    elif action == "rest":
        print(colored("you take a rest and regain your strengh.","blue"))
        health += 20
        if health > 100:
            health = 100
        print(colored("your current health is {health}","blue"))
        
    elif action == "trade": 
        if "map" in inventory:
            print(colored("you trade your map for a compass","green"))
            inventory.remove("map")
            inventory.append("compass")
        else : 
            print(colored("you have nothing to trade","yellow"))
        
    elif action == "find_clues":
        print(colored("you search the area and find an important clue!","yellow"))
        clues += 1
        print
        
        ....
        
        
    