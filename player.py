# Creating the player

class Player:
    def __init__(self, name, current_room, health, money, weapon, armor):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.money = money
        self.weapon = weapon
        self.armor = armor
        self.inventory = []