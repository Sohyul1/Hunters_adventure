# Aeron Dequito
# 02/24/2025
# A game about training


# Import random 
import random

# Make the user's stats
while True:
    user_atck = 5
    user_def = 3
    user_hp = 10

    # Make the list of monsters and their stats
    monsters_and_stats = [["Slime", 5, 5, 8], 
                        ["Goblin", 10, 8, 15], 
                        ["Orc", 16, 15, 25],
                        ["Minotaur", 25, 25, 50], 
                        ["Dragon", 45, 40, 100] ]

    # Ask thae player to start the game
    ans = input("Type enter to start the game: ").lower().strip()
    
    # Ask the player to choose between "train" or "fight"
    if ans == "enter":
        print('\nNote:\n"Train" will give you random addional stats.\n"Fight" is battling a random monster.')
        
        while True:
            choice = input("\nType 'Train' to gain stats\nType 'Fight' to battle an enemy: ").lower().strip()
            
    # Train - randomly increase the player's atck, def, and hp
            if choice == "train":
                atck_incr = random.randint(1, 10)
                def_incr = random.randint(1, 10)
                hp_incr = random.randint(1, 10)

                user_atck += atck_incr
                user_def += def_incr
                user_hp += hp_incr
                print("\nYou have increased your stats!")
                print(f"Attack increased: +{atck_incr}\nDefense increased: +{def_incr}\nHP increased: +{hp_incr}\n")
                print(f"Your current stats are:\nAttack:{user_atck}\nDefense:{user_def}\nHP:{user_hp}")
    
    # Fight -  will fight a random monster from the list created 
            elif choice == "fight":
                break
            else:
                print("Invalid input, please input a 'Train' or 'Fight'. ")
        
        enemy = random.choice(monsters_and_stats)
        enemy_name = enemy[0]
        enemy_atck = enemy[1]
        enemy_def = enemy [2]
        enemy_hp = enemy[3]

        print(f"\nA wild {enemy_name} appeared!!!")
        print(f"\nYour current stats are:\nAttack:{user_atck}\nDefense:{user_def}\nHP:{user_hp}")
        print(f"\nThe {enemy_name} stats are:\nAttack: {enemy_atck}\nDefense {enemy_def}\nHP: {enemy_hp}\n")
        print("Get ready to battle!\n")


    # Start of battle - player atcks first then monster (repeated until one of them dies )
        while user_hp > 0 and enemy_hp > 0:
            if user_atck > enemy_def:
                    user_dmg = user_atck - enemy_def
            else:
                user_dmg = 1

            enemy_hp -= user_dmg
            print(f"You dealt {user_dmg} to the {enemy_name}! Monster HP: {enemy_hp}\n")
        
            if enemy_hp <= 0:
                print(f"The {enemy_name} have died, You won!\n")
    
    # Player won - rank them base on the monster they defeated and display a congratulatory message
                if enemy_name == "Slime":
                    print("Congratulations! You are now a D-rank hunter!")
                elif enemy_name == "Goblin":
                    print("Congratulations! You are now a C-rank hunter!")
                elif enemy_name == "Orc":
                    print("Congratulations! You are now a B-rank hunter!")
                elif enemy_name == "Minotaur":
                    print("Congratulations! You are now an A-rank hunter!")
                elif enemy_name == "Dragon":
                    print("Congratulations! You are now an S-rank hunter!")
                break
            
            if enemy_atck > user_def:
                enemy_dmg = enemy_atck - user_def
            else:
                enemy_dmg = 1
            user_hp -= enemy_dmg
            print(f"\tThe {enemy_name} dealt {enemy_dmg} damage to you! Your HP:{user_hp}\n")
            
    # Monster won - display a death message
            if user_hp <= 0:
                    print(f"You have died in a the hand of a monster, you are still weak\n")

    # Ask for if they want to star a new life
        ans = input("\nThe game stops here, wanna play again? (yes/no) \n").lower().strip()
        if ans == "no":
            print("Thank you for playing the game!")
            break
