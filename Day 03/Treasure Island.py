print ("Welcome to Treasure Island.")
print ("Your Mission is to find the treasure.")
choice1 =input("You are at a crossroad, where do you want to go?"
               'Type "left" or "right".').lower()


if choice1 == "left":
    choice2 = input('You are come to a lake.'
                    'There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat'
                    'Type "swim" to swim across.\n').lower()

    if choice2 == "wait" :
        choice3 = input("You arrive at the island unharmed."
                          "There is house with 3 doors. one red,"
                          "one yellow and one blue."
                          "Which colour do you choose? \n").lower()
          
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
            
    else:
      print("You got attacked by an angry trout. Game Over.")


else:
   print("You fell in to a hole. Game Over.")