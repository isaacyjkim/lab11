import character

class Wizard(character.Character):

    """
    Concrete class representing a wizard character.
    """
    
    def description(self):
        """Returns a description of the wizard."""
        return "Altar the Wizard"
    
    def magic_resistance(self):
        """Returns the wizard's magic resistance."""
        return 3
    
    def strength(self):
        """Returns the wizard's attack power."""
        return 1