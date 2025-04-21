import abc 

class Character(abc.ABC): 

    @abc.abstractmethod
    def description(self): 
        """Returns a description of the character."""
        pass
        
    @abc.abstractmethod
    def magic_resistance(self): 
        """Returns the character's magic resistance."""
        pass

    @abc.abstractmethod
    def strength(self):
        """Returns the character's strength power."""
        pass

    def __str__(self): 
        """Returns a string representation of the character description, magic resistance and strength."""
        return f"{self.description()} Magic Resistance: {self.magic_resistance()} Strength: {self.strength()}"

