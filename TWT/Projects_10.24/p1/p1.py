name = input("Hey! Type your name: ")
print("Hello", name, ". Welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!")

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell off a cliff! Game Over, Try Again.")

    elif direction == "right":
        choice = input(
            "You come across a bridge with a troll underneath. 'What is the name of a weapon whose blade is double sided and curved?' (scimitar/greataxe) "
        ).lower()
        if choice == "scimitar":
            print("The troll eats you whole! Game Over.")
        else:
            print("That's correct! You are able to cross the bridge")

else:
    print("We are NOT playing...")
