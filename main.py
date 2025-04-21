from character import Character
from bard import Bard
from warrior import Warrior
from wizard import Wizard
from decorator import Decorator
from shield import Shield
from cloak import Cloak
from ring import Ring
import check_input 
import random

def main():
    monsters = [
        ['Spiked Dragon', 0, 6],
        ['Orc Warlord', 1, 5],
        ['Shadow Knight', 2, 4],
        ['Lava Monster', 3, 3],
        ['Fiendish Ghoul', 4, 2],
        ['Goblin Mage', 5, 1],
        ['Dark Magician', 6, 0],
    ]

    print("Character Maker! ")
    print("Choose a starting character:\n1. Bard\n2. Warrior\n3. Wizard")
    character_choice = check_input.get_int_range("> ", 1, 3) 
    if character_choice == 1:
        character = Bard()
    elif character_choice == 2:
        character = Warrior()
    else:
        character = Wizard()
    print(character)

    items=['Sturdy Shield', 'Magic Ring', 'Protective Cloak']
    for i in range(2):
        print(f'Choose {len(items)-1} items:')
        for j, item in enumerate(items):
            print(f'{j+1}. {item}')
        item_choice = items[check_input.get_int_range("> ", 1, len(items))-1]
        
        if item_choice == 'Sturdy Shield':
            character = Shield(character)
        elif item_choice == 'Magic Ring':
            character = Ring(character)
        else:
            character = Cloak(character)
        items.remove(item_choice)
        print(f'\n{character}')

    print('You must pass two of the following three trials!')
    trials = 0
    for i in range(3):
        print(f'Trial {i+1} of 3:')
        monster = random.choice(monsters)
        print(f'You encounter a {monster[0]}')
        print(f'MR: {monster[1]}')
        print(f'STR: {monster[2]}')
        print('Fight:\n1. Battle\n2. Dodge')
        choice = check_input.get_int_range("> ", 1, 2)
        if choice == 1:
            print(f'You battle with the {monster[0]} and easily defeat it.\n You have passed this trial')
            trials+=1
        else:
            print(f'You attempt to dodge the {monster[0]}, but it manage to hit you.\nYou have failed this trial.')

    if trials == 2:
        print('\nYou have passed the three trials...barely.')
    elif trials == 3:
        print('\nYou have successfully passed all trials.')
    else:
        print('\nYou have failed.')        
    

main()