from decorator import Decorator 
""""
Ring class that extends the Decorator class.
"""
class Ring(Decorator):
    def description(self):
        # Add the ring description to the base description
        return 'Ringed' + super().description() 
    
    def magic_resistance(self):
        # Increase the magic resistance by 2
        return super().magic_resistance() + 2
    
    def strength(self):
        # Increase the strength by 0
        return super().strength() 
    
    