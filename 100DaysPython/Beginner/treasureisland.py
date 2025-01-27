import sys

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure!\n")

direction = input("You're at a fork in the dungeon. Do you go left, or do you go right? ").lower()


if direction == "left":
    pit = input("There's a spike pit ahead. Do you take the jump, or wait and see? ").lower()
    if pit == "jump":
        door = input("There are three doors in sight. A Red one, a Blue one, and a Yellow one. You may only choose one. Make your decision. ").lower()
        if door == "yellow":
            print("Congratulations! You've found the treasure! You're free to loot anything you see.")
        elif door == "red":
            print("The room is engulfed in flames! GAME OVER")
            sys.exit(1)
        elif door == "blue":
            print("The room suddenly freezes all of time and space! GAME OVER")
            sys.exit(1)
        else:
            print("You chose a non-existing door. GAME OVER")
    else:
        print("The floor beneath you crumbles! GAME OVER")
        sys.exit(1)
else:
    print("You find yourself staring at an undead warrior with axe in hand. GAME OVER")
    sys.exit(1)
