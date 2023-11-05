class Player:
    def __init__(self):
        self.name = "Unnamed Hero"
        self.exp = 0
        self.world_stats = {
            'level': 1,
            'health': 100,
            'mana': 50,
            'gold': 10,
            'JC': 0,
        }
        self.combat_stats = {
            'Strength': 0,
            'Endurance': 0,
            'Intellect': 0,
            'Stealth': 0,
            'Charm': 0,
            'Luck': 0,
            'Fire Defense': 0,
            'Earth Defense': 0,
            'Water Defense': 0,
            'Wind Defense': 0,
            'Dark Defense': 0,
            'Light Defense': 0,
        }
        self.equipped_items = {
            'Weapon': "Straight Sword",
            'Armor': "Iron Mail",
            'Shield': "Iron Shield",
            'Misc': None
        }
        self.inventory = {
            'Weapons': [],
            'Armors': [],
            'Shields': [],
            'Misc': []
        }
        self.storage = {
            'Weapons': [],
            'Armors': [],
            'Shields': [],
            'Misc': []
        }

    def display_world_stats(self):
        print("\nCharacter Status:")
        print(f"Name: {self.name}")
        for stat, value in self.world_stats.items():
            print(f"{stat}: {value}")
        print("\n")

    def display_combat_stats(self):
        print("\nCombat Stats:")
        print(f"Health: {self.world_stats['health']}")  # Show current health
        print(f"Mana: {self.world_stats['mana']}")  # Show current mana
        for stat, value in self.combat_stats.items():
            print(f"{stat}: {value}")
        print("\n")

    def level_up_stat(self):
        print("Select the stat you wish to level up:")
        print("(S)trength, (I)ntellect, (St)ealth, (C)harm, (L)uck")

        stat_choice = input("Enter your choice: ").lower()
        if stat_choice == 's':
            self.combat_stats['Strength'] += 5
            print("Strength increased by 5.")
        elif stat_choice == 'i':
            self.combat_stats['Intellect'] += 5
            print("Intellect increased by 5.")
        elif stat_choice == 'st':
            self.combat_stats['Stealth'] += 5
            print("Stealth increased by 5.")
        elif stat_choice == 'c':
            self.combat_stats['Charm'] += 5
            print("Charm increased by 5.")
        elif stat_choice == 'l':
            self.combat_stats['Luck'] += 5
            print("Luck increased by 5.")
        else:
            print("Invalid selection. Stat not increased.")

        # After updating, show the updated stats
        self.display_combat_stats()
    def gain_exp(self, amount):
        """Handles the player gaining experience and leveling up if enough exp is gained."""
        self.exp += amount
        print(f"You gained {amount} experience points!")

        # Define the experience threshold for leveling up
        level_up_threshold = 15  # This can be more complex, based on the current level, if desired

        if self.exp >= level_up_threshold:
            self.world_stats['level'] += 1  # Increment the player's level
            self.exp = 0  # Reset experience points after leveling up
            print(f"You have leveled up to level {self.world_stats['level']}!\n")
            self.level_up_stat()  # Prompt the player to level up a stat
