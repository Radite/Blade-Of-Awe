# Simple text-based fantasy adventure game

#Introduction
print("Welcome to the Quest for the Blade of Awe!")
print("Your journey begins in the humble village of Dworgon, as a young Warrior seeking the legendary Blade of Awe...\n")

#Character Creation
player_name = input("Enter your name, brave warrior: ")
print(f"\nGreetings, {player_name}. Your journey awaits!\n")

# Initial Character Stats
health = 100
mana = 50
gold = 10
JC = 0

equipped_items = {
    'Weapon': "Straight Sword",
    'Armor': "Iron Mail",
    'Shield': "Iron Shield",
    'Misc': None
}


inventory = {
    'Weapons': [],
    'Armors': [],
    'Shields': [],
    'Misc': []
}
Storage = {
    'Weapons': [],
    'Armors': [],
    'Shields': [],
    'Misc': []
}

# Function to display character status with the categorized inventory
def display_status():
    print("\nCharacter Status:")
    print(f"Name: {player_name}")
    print(f"Health: {health}")
    print(f"Mana: {mana}")
    print(f"Gold: {gold}")
    print("\nInventory:")
    print("\nEquipped Items:")
    for category, item in equipped_items.items():
        print(f"{category.capitalize()}: {item if item else 'None'}")
    print("\n")

#Function to equip an item
def equip_item(category, item):
    # Check if the category is valid and the item is in the inventory
    if category in inventory and item in inventory[category]:
        # If there's already an item equipped in the category, put it back into the inventory
        if equipped_items[category] is not None:
            inventory[category].append(equipped_items[category])
            print(f"You have unequipped the {equipped_items[category]} and put it back into your inventory.")
        
        # Equip the new item and remove it from the inventory
        equipped_items[category] = item
        inventory[category].remove(item)
        print(f"You have equipped the {item}.")
    else:
        print("You cannot equip this item.")

# Function for a combat encounter
def combat():
    global health
    enemy_health = 30
    print("A wild goblin appears!\n")

    while enemy_health > 0:
        action = input("Do you want to (A)ttack, use (M)agic, or (R)un away? ").lower()

        if action == "a":
            print("You attack the goblin!")
            enemy_health -= 10
            # Check if the goblin's health has dropped to 0 or less
            if enemy_health <= 0:
                print("The goblin has fainted. You win!\n")
                break
            else:
                print(f"The goblin has {enemy_health} health left.\n")
        elif action == "m":
            print("You cast a fireball!")
            enemy_health -= 15
            # Check if the goblin's health has dropped to 0 or less
            if enemy_health <= 0:
                print("The goblin has fainted. You win!\n")
                break
            else:
                print(f"The goblin has {enemy_health} health left.\n")
        elif action == "r":
            print("You run away from the goblin!")
            return
        else:
            print("Invalid action. Try again.")

        # Goblin's turn
        if enemy_health > 0:
            print("The goblin attacks you!")
            health -= 10
            if health <= 0:
                print("You have been defeated by the goblin!")
                exit()
# Game Loop
while True:
    action = input("What would you like to do? (E)xplore, (R)est, (C)heck inventory, or (Q)uit: ").lower()
    
    if action == "e":
        combat()
    elif action == "r":
        health = 100
        print("You have rested and restored your health.")
    elif action == "c":
        display_status()
    elif action == "q":
        print("Thank you for playing. Farewell!")
        break
    else:
        print("Invalid action. Please choose again.")
