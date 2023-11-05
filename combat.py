def initiate_combat(player):
    enemy_health = 30
    print("A wild goblin appears!\n")

    while enemy_health > 0 and player.world_stats["health"] > 0:
        action = input("Do you want to (A)ttack, use (M)agic, (D)isplay Stats or (R)un away? ").lower()

        if action == "a":
            print("You attack the goblin!")
            enemy_health -= 10  # Example value, should be based on player's combat stats
            if enemy_health <= 0:
                print("The goblin has fainted. You win!\n")
                player.world_stats['gold'] += 5  # Reward
                break
            else:
                print(f"The goblin has {enemy_health} health left.\n")

        elif action == "m":
            if player.world_stats["mana"] >= 10:  # Example mana cost
                player.world_stats["mana"] -= 10
                print("You cast a fireball!")
                enemy_health -= 15  # Example value, should be based on player's combat stats
                if enemy_health <= 0:
                    print("The goblin has fainted. You win!\n")
                    player.world_stats['gold'] += 5  # Reward
                    player.gain_exp(5)  # Reward the player with experience, this checks for level up internally




                    break
                else:
                    print(f"The goblin has {enemy_health} health left.\n")
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

        # Goblin's turn
        print("The goblin attacks you!")
        player.world_stats["health"] -= 5  # Example value, should be modified based on player's defense stats
        if player.world_stats["health"] <= 0:
            print("You have been defeated by the goblin!")
            return  # End the combat if the player is defeated
