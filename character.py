class Character():
    def __init__(self) -> None:
        self.name: str = ""
        self.level: int = 1
        self.race: str = ""
        self.health: int = 0
        self.magic: int = 0
        self.energy: int = 0
        self.inventory: list = []
        
    def do_damage(self, enemy):
        pass