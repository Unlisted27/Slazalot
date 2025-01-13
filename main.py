import os
import time
import basicrpg
import assets
import assets.characters
import assets.game_entities
import assets.utils
assets.utils.clear_screen()
print("Hello player, welcome to")
class screens():
    def __init__(self):
        pass
    def home_screen():
        assets.utils.clear_screen()
        print(r'''  _________.____       _____  __________  _____  .____    ___________________
 /   _____/|    |     /  _  \ \____    / /  _  \ |    |   \_____  \__    ___/
 \_____  \ |    |    /  /_\  \  /     / /  /_\  \|    |    /   |   \|    |   
 /        \|    |___/    |    \/     /_/    |    \    |___/    |    \    |   
/_______  /|_______ \____|__  /_______ \____|__  /_______ \_______  /____|   
        \/         \/       \/        \/       \/        \/       \/         ''')
        ans = assets.utils.menu("OPTIONS",["PLAY","EXIT","SETTINGS"])
        if ans == "PLAY":
            screens.char_creator()
        elif ans == "EXIT":
            exit()
        elif ans == "SETTINGS":
            input("SETTINGS COMING SOON")
            screens.home_screen()
    def char_creator():
        player = assets.characters.player
        player.name = input("Player name: ")
        for i in range(3):
            print("Randomising stats \ ",end="\r")
            time.sleep(0.2)
            print("Randomising stats |",end="\r")
            time.sleep(0.2)
            print("Randomising stats / ",end="\r")
            time.sleep(0.2)
            print("Randomising stats - ",end="\r")
            time.sleep(0.2)
        player.create_random()
        assets.utils.clear_screen()
        player.printstats()
        input("Continue to weapon selection?")
        assets.utils.clear_screen()
        ans = assets.utils.menu("CHOOSE YOUR WEAPON",["Sword","Mase","Battleaxe"])
        if ans == "Sword": player.equip_weapon(assets.game_entities.items.weapons.sword)
        if ans == "Mase": player.equip_weapon(assets.game_entities.items.weapons.mase)
        if ans == "Battleaxe": player.equip_weapon(assets.game_entities.items.weapons.battleaxe)
        input()
        assets.utils.clear_screen()
        player.printinvent()
    def combattest():
        assets.utils._combat([assets.characters.player,assets.characters.companion,assets.characters.goblin])
    def test():
        assets.utils.gen_character(assets.game_entities.races,assets.game_entities.professions)
screens.home_screen()
screens.test()