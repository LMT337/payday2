from payday2.players import Character
from payday2.weapons import Weapon
# Example:

print("Choose your character: \n")
###### List choices here #######
in_string = input()
if input == '1':
    character = Character('Hoxton')
elif input == '2':
    character = Character('Jimmy')
elif input == '3':
    character = Character('Sydney')
elif input == '4':
    ###### write the code to add character Dallas ######
    pass
else:
    ###### what do we do if 1-4 wasn't selected? ######
    pass

###### Print out a welcome statement ######

print("Choose your weapon:")

###### Add code to select a weapon, similar to the character class above ######
###### Hint: use the "Weapon" class
