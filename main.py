from Player import Player
import combat

def main():
    print("Welcome to the Quest for the Blade of Awe!")
    # Initialize the player
    player = Player()
    player.name = input("Enter your name, brave warrior: ")
    print(f"\nGreetings, {player.name}. Your journey awaits!\n")

    # Main game loop
    while True:
        action = input("What would you like to do? (E)xplore, (R)est, (C)heck stats, or (Q)uit: ").lower()
        
        if action == "e":
            combat.initiate_combat(player)
        elif action == "r":
            player.rest()  # Restores to full health and mana based on max values
        elif action == "c":
            player.display_world_stats()
            player.display_combat_stats()
        elif action == "q":
            print("Thank you for playing. Farewell!")
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
