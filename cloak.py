from decorator import Decorator 

""""
Cloak class that extends the Decorator class.
"""
class Cloak(Decorator):
    def description(self):
        # Add the cloak description to the base description
        return 'Cloaked ' + super().description()
    
    def magic_resistance(self):
        # Increase the magic resistance by 1
        return super().magic_resistance() + 1
    
    def strength(self):
        # Increase the strength by 1
        return super().strength() + 1
    
    