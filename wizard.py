import character

class Wizard(character.Character):

    def description(self):
        """Returns a description of the wizard."""
        return "Yo ima wizard. zshsshshh woooo."
    
    def magic_resistance(self):
        """Returns the wizard's magic resistance."""
        return 3
    
    def strength(self):
        """Returns the wizard's attack power."""
        return 1