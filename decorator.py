from character import Character

class Decorator(Character):
    def __init__(self, c):
        self._char = c

    def description(self):
        return self._char.description()
    
    def magic_resistance(self):
        return self._char.magic_resistance()
    
    def strength(self):
        return self._char.strength()
    
    def __str__(self):
        return self._char.__str__()
