from character import Character

"""
Decorator class for character objects.
"""

class Decorator(Character):
    def __init__(self, c):
        # Decorator constructor
        self._char = c

    def description(self):
        """Returns a description of the character."""
        return self._char.description()
    
    def magic_resistance(self):
        """Returns the character's magic resistance."""
        return self._char.magic_resistance()
    
    def strength(self):
        """Returns the character's attack power."""
        return self._char.strength()
    
    def __str__(self):
        """Returns a string representation of the character."""
        return super().__str__()
