import random


class SuperHero:
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense * .10

    def attack_turn(self):
        attack_power = self.damage + random.randint(1, 20)
        return attack_power

    def take_damage(self, received_damage):
        damage_taken = received_damage * self.defense
        self.health -= damage_taken

name = input("Enter your super hero 1's name: ")
health = int(input("Enter your super hero 1's health: "))
damage = int(input("Enter your super hero 1's damage: "))
defense = int(input("Enter your super hero 1's defense 3-7: "))

super_1 = SuperHero(name, health, damage, defense)


name = input("Enter your super hero 2's name: ")
health = int(input("Enter your super hero 2's health: "))
damage = int(input("Enter your super hero 2's damage: "))
defense = int(input("Enter your super hero 2's defense 3-7: "))

super_2 = SuperHero(name, health, damage, defense)



while True:
    print(f"\n{super_1.name}'s turn ----------------------------")

    super_1_damage_roll = super_1.attack_turn()
    print(f"{super_1.name} attacks for {super_1_damage_roll}\n")
    
    super_2.take_damage(super_1_damage_roll)

    print(f"{super_2.name} now has {super_2.health} remaining\n")

    if super_2.health <= 0:
        print(f"{super_1.name} wins!")
        break

    
    print(f"\n{super_2.name}'s turn ----------------------------")

    super_2_damage_roll = super_2.attack_turn()
    print(f"{super_2.name} attacks for {super_2_damage_roll}")
    
    super_1.take_damage(super_2_damage_roll)

    print(f"{super_1.name} now has {super_1.health} remaining")

    if super_1.health <= 0:
        print(f"{super_2.name} wins!")
        break

    


'abc'.upper()

