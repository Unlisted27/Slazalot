#General functions
import basicrpg,os,random
from assets import game_entities

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def gen_character(race_lib,prof_lib):
    #char = basicrpg.character(race_lib.human)
    races = dict(vars(race_lib))#Gets all of the objects from the race library
    professions = dict(vars(prof_lib)) #Ditto
    races.pop("__module__")
    races.pop("__dict__")
    races.pop("__weakref__")
    races.pop("__doc__")
    professions.pop("__module__")
    professions.pop("__dict__")
    professions.pop("__weakref__")
    professions.pop("__doc__")

    #print(races)
    #print(professions)
    #Get random values
    race_name,race = random.choice(list(races.items()))
    profession_name,profession = random.choice(list(professions.items()))
    character = basicrpg.character(race,profession,basicrpg.genname())
    character.create_random()
    return(character)

    #print(vars(race_lib))
def _combat(characters:list): #UNUSED
    """characters is a list of character objects"""
    combat_order = {}
    clear_screen()
    print("----------------")
    print("THE FIGHT BEGINS")
    print("----------------")
    try:
        initiative = 0
        for item in characters:
            #print(f"{item.name} has joined the fight")
            initiative = basicrpg.roll(1, 20)
            combat_order.update({item: initiative})
        # Sort characters by their initiative in combat_order
        characters.sort(key=lambda char: combat_order.get(char, 0), reverse=True) #ummm IDK how this works, but it do. Not questioning it
        i = 1
        for char in characters:
            print(f"[{i}]{char.name} | {char.race.name}")
            i+=1
        for char in characters:
            print(f"It is {char.name}'s turn")

    except Exception as e:
        print(e)
class random_encounter():
    ["Character interaction","Obstacle: log on road","Combat","Riddle, puzzle, or toll","random side quest"]
    #def combat(): #A random combat encounter
        #pass
    def character_interaction(): #Character interaction
        pass
    def obstacle(): #Random obstacle blocking your path
        pass
    def toll(): #Toll can be a riddle, puzzle, or road toll
        pass