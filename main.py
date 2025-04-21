from character import Character
from bard import Bard
from warrior import Warrior
from wizard import Wizard
from decorator import Decorator
from shield import Shield
from cloak import Cloak
from ring import Ring
import check_input 

def main():
    monsters = {
        ['Spiked Dragon', 0, 6]
        ['Orc Warlord', 1, 5]
        ['Shadow Knight', 2, 4]
        ['Lava Monster', 3, 3]
        ['Fiendish Ghoul', 4, 2]
        ['Goblin Mage', 5, 1]
        ['Dark Magician', 6, 0]
    }
    

    

    print("Character Maker! ")
    print("Choose a starting character:\n1. Bard\n2. Warrior\n3. Wizard")
    character_choice = check_input.check_input("> ", 1, 3) 
    if character_choice == 1:
        character = Bard()
    elif character_choice == 2:
        character = Warrior()
    else:
        character = Wizard()

    print(character)

main()