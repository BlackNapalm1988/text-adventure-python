from character import Character

class Enemy(Character):
    def __init__(self):
        Character.__init__(self, player)
        self.tough_factor = randint(0, player.level)
    def goblin(self):
        self.level: int = 1
        self.name: str = "A Goblin"
        self.health: int = randint(1, player.health * self.tough_factor)
    def troll(self):
        self.level: int = 1
        self.name: str = "A Troll"
        self.health: int = randint(2, player.health * self.tough_factor)