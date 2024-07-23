from termcolor import colored  #terminalde renklendirme
from utils import choices_to_str

choices = ["sleep", "cheer", "dowork","gohouse"]
inventory = []

# The `colored` function prints out text in the color provided!
print(colored("Hello! Welcome to a boring adventure!", "green"))
print(colored("You are in a dark room. Choose one of the following:", "blue"))

# done is a "boolean variable" (i.e., either True or False)
# We use it to control when the `while` loop should end!
done = False
while not done:
    # `choices_to_str` is a function we wrote to turn a choices
    # list into a string where each choice is underlined.  If you
    # want to check it out, it's in `utils.py` on the left!
    prompt = choices_to_str(choices)
    action = input(prompt + " >>> ")
    if action == "sleep" and ("work" and "interhouse") in inventory:
        print(colored("ZZZZ...zzzz", "blue"))
        done = True
    elif action == "sleep":
        print(colored("You still have work or task to do!", "red"))
    elif action == "dowork":
        inventory.append("work")
        print(colored("You're done with your work now!", "green"))
    elif action == "gohouse":
        inventory.append("interhouse")
        print(colored("you went to interhouse!!!","green"))
    elif action == "cheer":
        print("Hip hip hooray!! You're still tired!")
print(colored("The adventure is over!", "green"))








