# Import random 
import random

# Make the user's stats
user_atck = 1
user_def = 3
user_hp = 10

# Make the list of monsters and their stats
monsters_and_stats = [["Slime", 1, 5, 8], 
                      ["Goblin", 5, 8, 15], 
                      ["Orc", 10, 15, 20],
                      ["Minotaur", 15, 20, 25], 
                      ["Dragon", 20, 25, 50] ]

# Ask thae player to start the game
ans = input("Type enter to start the game: ").lower().strip()
# Ask the player to choose between "train" or "fight"
if ans == "enter":
    print('Note:"Train" will give you random addional stats.\n     "Fight" is battling a random monster.')
    
    while True:
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
            enemy = random.choice(monsters_and_stats)
            enemy_name = enemy[0]
            enemy_atck = enemy[1]
            enemy_def = enemy [2]
            enemy_hp = enemy[3]

            print(f"A wild {enemy_name} appeared!!!")
            print("Get ready to battle!")


# Start of battle - player atcks first then monster(repeated until one of them dies )
            while user_hp > 0 and enemy_hp > 0:
                if user_atck > enemy_def:
                    user_dmg = user_atck - enemy_def
                else:
                    user_dmg = 0

                    enemy_hp -= user_dmg
                    print(f"You dealt {user_def} to the {enemy_name}!")
                    print(f"The {enemy_name} is now {enemy_hp} HP!")


                if enemy_atck > user_def:
                    enemy_dmg = enemy_atck - user_def
                else:
                    enemy_dmg = 0

                    user_hp -= enemy_dmg
                    print(f"The {enemy_name} dealt {enemy_dmg} damage to you!")
                    print (f"You are now {user_hp} HP!")
                 












# Player won - rank them base on the monster they defeated and display a congratulatory message
# Monster won - display a death message
# Ask for if they want to star a new life