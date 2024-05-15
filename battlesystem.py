import random

class Soldier:
    def __init__(self, name, strength, speed, ability, stealth, intelligence):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.ability = ability
        self.stealth = stealth
        self.intelligence = intelligence
        self.hp = 100  # Initial hit points
        
    def attack(self, opponent, terrain_advantage):
        damage = random.randint(1, self.strength)
        if terrain_advantage:
            damage *= 1.05  # Apply 5% advantage for terrain1 or 6% for terrain2
        opponent.hp -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage.")
        
    def is_alive(self):
        return self.hp > 0

class Army:
    def __init__(self, name, soldiers):
        self.name = name
        self.soldiers = soldiers
        
    def all_alive(self):
        return all(soldier.is_alive() for soldier in self.soldiers)
        
def battle(army1, army2, terrain):
    print(f"Battle between {army1.name} and {army2.name} begins on {terrain} terrain!\n")
    round_number = 1
    while army1.all_alive() and army2.all_alive():
        print(f"Round {round_number}:")
        for soldier1 in army1.soldiers:
            if army2.all_alive():
                # Select random opponent from army2
                opponent = random.choice(army2.soldiers)
                if opponent.is_alive():
                    soldier1.attack(opponent, terrain == 'terrain1')
        for soldier2 in army2.soldiers:
            if army1.all_alive():
                # Select random opponent from army1
                opponent = random.choice(army1.soldiers)
                if opponent.is_alive():
                    soldier2.attack(opponent, terrain == 'terrain2')
        round_number += 1
    print("\nBattle ends!")
    if army1.all_alive():
        print(f"{army2.name} has been defeated!")
    else:
        print(f"{army1.name} has been defeated!")

# Create soldiers for Army 1
soldiers_army1 = [
    Soldier("Soldier A1", strength=10, speed=8, ability=7, stealth=5, intelligence=6),
    Soldier("Soldier A2", strength=9, speed=7, ability=6, stealth=8, intelligence=5),
    Soldier("Soldier A3", strength=8, speed=9, ability=5, stealth=6, intelligence=7)
]
# Create soldiers for Army 2
soldiers_army2 = [
    Soldier("Soldier B1", strength=10, speed=8, ability=7, stealth=5, intelligence=6),
    Soldier("Soldier B2", strength=9, speed=7, ability=6, stealth=8, intelligence=5),
    Soldier("Soldier B3", strength=8, speed=9, ability=5, stealth=6, intelligence=7)
]

"""
# Create armies
army1 = Army("Army 1", soldiers_army1)
army2 = Army("Army 2", soldiers_army2)

# Start the battle with different terrains
battle(army1, army2, terrain='terrain1')
battle(army1, army2, terrain='terrain2')
"""

def simulate_battle(army1, army2, terrain, num_simulations):
    army1_wins = 0
    for _ in range(num_simulations):
        army1_copy = Army(army1.name, [Soldier(soldier.name, soldier.strength, soldier.speed, soldier.ability,
                                                soldier.stealth, soldier.intelligence) for soldier in army1.soldiers])
        army2_copy = Army(army2.name, [Soldier(soldier.name, soldier.strength, soldier.speed, soldier.ability,
                                                soldier.stealth, soldier.intelligence) for soldier in army2.soldiers])
        battle(army1_copy, army2_copy, terrain)
        if army1_copy.all_alive():
            army1_wins += 1
    return army1_wins / num_simulations

# Define the armies and terrain
army1 = Army("Army 1", soldiers_army1)
army2 = Army("Army 2", soldiers_army2)
terrain = 'terrain2'
num_simulations = 10000

# Simulate the battle and calculate the probability of Army 1 winning
probability_army1_wins = simulate_battle(army1, army2, terrain, num_simulations)
print(f"The probability of Army 1 winning the battle on {terrain} is: {probability_army1_wins:.2f}")

