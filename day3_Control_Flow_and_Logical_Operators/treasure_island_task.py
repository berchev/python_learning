# Single quotes allows you to create a multiple lines of string

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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# using backslash as an escape character
left_or_right = input('You\'re in a crossroad, where do you want to go? \n Type "left" or "right". \n')

if left_or_right == "left" or left_or_right == "Left":
    swim_or_wait = input('You\'ve come to a lake. There is an island in the middle of the lake? \n Type "wait" to wait for a boat or "swim" to swim across. \n')
    
    if swim_or_wait == "wait" or swim_or_wait == "Wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose? \n")

        if door == "yellow" or door == "Yellow":
            print("You win!")
        elif door == "blue" or "Blue":
            print("Eaten by beasts. Game Over.")
        elif door == "red" or door == "Red":
            print("Burned by fire. Game Over.")
        else:
            print("Game Over.")
    
    # elif swim_or_wait == "swim" or swim_or_wait == "Swim":
    #     print("Attacked by trout. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
# elif left_or_right == "right" or left_or_right == "Right":
#     print("Fell into a hole. Game Over")
else:
    print("Fell into a hole. Game Over")