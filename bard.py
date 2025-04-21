import character

class Bard(character.Character): 

    def description(self): 
        """Returns a description of the bard."""
        return "Yo ima bard. What's a bard? "
    
    def magic_resistance(self): 
        """Returns the bard's magic resistance."""
        return 2
    
    def strength(self):
        """Returns the bard's attack power."""
        return 2 