from character import Character

class Player(Character):

    def __init__(self) -> None:
        Character.__init__(self)
        self.level = 1

    def text_input(self) -> str:

        text = input (">> ")
        text = text.lower()
        text = text.strip()

        return text
 
    def set_stats(self, **stats):

        for key, value in stats.items():
            if key == "name":
                self.name = value
            if key == "race":
                self.race = value
            if key == "hp":
                self.health = value
            if key == "mp":
                self.magic = value
            if key == "energy":
                self.energy = value
            if key == "level":
                self.level = value