import random

def initiate_combat(player):
    enemy_health = 30
    print("A wild goblin appears!\n")
    combat_over = False  # Flag to check if combat has ended

    while enemy_health > 0 and player.world_stats["health"] > 0:
        action = input("Do you want to (A)ttack, use (M)agic, (D)isplay Stats or (R)un away? ").lower()

        if action == "a":
            base_damage = 10  # Example base damage for a physical attack
            damage = player.calculate_damage(base_damage)
            enemy_health -= damage
            print(f"You dealt {damage} damage to the goblin!")

        elif action == "m":
            base_damage = 15  # Example base damage for a magic attack
            if player.world_stats["mana"] >= 10:  # Example mana cost
                damage = player.calculate_damage(base_damage, is_magic=True)
                player.world_stats["mana"] -= 10
                print("You cast a fireball!")
                enemy_health -= damage
                print(f"You cast a spell dealing {damage} magic damage to the goblin!")
            else:
                print("Not enough mana!\n")

        elif action == "d":
            player.display_combat_stats()
            continue  # Skip the goblin's turn

        elif action == "r":
            print("You run away from the goblin!")
            return

        else:
            print("Invalid action. Try again.")
            continue  # Skip the goblin's turn

        # Check if goblin is defeated
        if enemy_health <= 0:
            print("The goblin has fainted. You win!\n")
            combat_over = True  # Combat ends when the goblin is defeated
            break  # Break out of combat loop

        # Goblin's turn if not defeated
        if random.random() < player.calculate_dodge_chance() / 100:
            print("You dodged the goblin's attack!")
        else:
            print("The goblin attacks you!")
            player.world_stats["health"] -= 5  # Example value, should be modified based on player's defense stats
            if player.world_stats["health"] <= 0:
                print("You have been defeated by the goblin!")
                return  # End the combat if the player is defeated

    # After combat loop
    if combat_over:
        # Rewards for defeating the goblin
        player.world_stats['gold'] += 5  # Reward the player with gold
        player.gain_exp(55)  # Reward the player with experience
        # Level-up check should be inside the gain_exp() method

