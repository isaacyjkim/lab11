import character

class Warrior(character.Character):

    """Concrete Class representing a warrior character."""

    def description(self):
        """Returns a description of the bard."""
        return "Harcor the Warrior"
    
    def magic_resistance(self):
        """Returns the bard's magic resistance."""
        return 0
    
    def strength(self):
        """Returns the bard's attack power."""
        return 4