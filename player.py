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

    
    # Player Movement
    def move_player(self, command):
        if getattr(self.current_room, f'{command}_to') is not None:
            self.current_room = getattr(self.current_room, f'{command}_to')
        else:
            print(f'YOU CAN NOT GO THAT WAY')

    