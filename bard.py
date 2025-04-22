import character

class Bard(character.Character): 

    """Concrete class representing a bard character."""

    def description(self): 
        """Returns a description of the bard."""
        return "Barth the Bard "
    
    def magic_resistance(self): 
        """Returns the bard's magic resistance."""
        return 2
    
    def strength(self):
        """Returns the bard's attack power."""
        return 2 
    
    
    