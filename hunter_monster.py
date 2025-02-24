# Import random 
import random
# Make the user's stats
user_atck = 1
user_def = 3
user_hp = 10
# Make the list of monsters and their stats
monsters_and_stats = ["Slime", "Goblin", "Orc","Minotaur", "Dragon", ]
# Ask thae player to start the game
ans = input("Type enter to start the game: ").lower().strip()
# Ask the player to choose between "train" or "fight"
if ans == "enter":
    choice = input("What would you like to do, 'Train' or 'Fight': ").lower().strip()
    
# Train - randomly increase the player's atck, def, and hp
    if choice == "train":
        atck_incr = random.randint(1, 10)
        def_incr = random.randint(1, 10)
        hp_incr = random.randint(1, 10)

        user_atck += atck_incr
        user_def += def_incr
        user_hp += hp_incr
        print(f"You have gained {atck_incr} Attack, {def_incr} Defense, and {hp_incr} HP")
        print(f"Your current stats are:\nAttack:{user_atck}\nDefense:{user_def}\nHP:{user_hp}")
# Fight -  will fight a random monster from the list created 
    elif choice == "fight":
        print("haha")


# Start of battle - player atcks first then monster(repeated until one of them dies )
# Player won - rank them base on the monster they defeated and display a congratulatory message
# Monster won - display a death message
# Ask for if they want to star a new life