
import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.inventory = []

    def display_stats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nInventory: {', '.join(self.inventory)}")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

def introduction():
    print("Welcome to the RPG Text Adventure!")
    time.sleep(1)
    print("You find yourself in a mysterious land...")
    time.sleep(1)
    print("Your adventure begins!")

def encounter_enemy(player):
    enemy = Enemy("Goblin", 20, 8)
    print(f"You encounter a {enemy.name}!")
    time.sleep(1)

    while player.health > 0 and enemy.health > 0:
        print("\n--- Battle Options ---")
        print("1. Attack")
        print("2. Use item")
        choice = input("Choose your action: ")

        if choice == "1":
            enemy.health -= player.attack
            print(f"You attack the {enemy.name} and deal {player.attack} damage!")
            time.sleep(1)

            player.health -= enemy.attack
            print(f"The {enemy.name} counterattacks and deals {enemy.attack} damage to you!")
            time.sleep(1)

        elif choice == "2":
            if player.inventory:
                item = random.choice(player.inventory)
                player.inventory.remove(item)
                print(f"You use {item} during the battle!")
                time.sleep(1)

                # Custom logic for using an item (you can expand this)

            else:
                print("You have no items in your inventory.")

        else:
            print("Invalid choice. Try again.")

    if player.health <= 0:
        print("Game over! You were defeated.")
        exit()
    else:
        print(f"You defeated the {enemy.name}! You gained experience points.")
        # Custom logic for gaining experience (you can expand this)

def main():
    introduction()

    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    while True:
        player.display_stats()
        print("\n--- Main Menu ---")
        print("1. Continue the journey")
        print("2. View inventory")
        print("3. Quit")
        choice = input("Choose your action: ")

        if choice == "1":
            encounter_enemy(player)

        elif choice == "2":
            print("Inventory:", ', '.join(player.inventory))

        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            exit()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
