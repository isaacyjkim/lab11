import abc 

class Character(abc.ABC): 

    """
    Abstract interface for character object. 
    """
    
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
        return f"{self.description()} \nMR: {self.magic_resistance()} \nSTR: {self.strength()}"

