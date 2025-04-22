from decorator import Decorator 

class Shield(Decorator):
    """
    Shield class that extends the Decorator class.
    """
    def description(self):
        # Add the shield description to the base description
        return 'Shielded' + super().description() 
    
    def magic_resistance(self):
        # Increase the magic resistance by 0
        return super().magic_resistance() 
    
    def strength(self):
        # Increase the strength by 2
        return super().strength() + 2
    
    