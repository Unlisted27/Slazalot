import os
import time
import basicrpg
import assets
import assets.characters
import assets.utils
assets.utils.clear_screen()
print("Hello player, welcome to")
class screens():
    def __init__(self):
        pass
    def home_screen():
        print(r'''  _________.____       _____  __________  _____  .____    ___________________
 /   _____/|    |     /  _  \ \____    / /  _  \ |    |   \_____  \__    ___/
 \_____  \ |    |    /  /_\  \  /     / /  /_\  \|    |    /   |   \|    |   
 /        \|    |___/    |    \/     /_/    |    \    |___/    |    \    |   
/_______  /|_______ \____|__  /_______ \____|__  /_______ \_______  /____|   
        \/         \/       \/        \/       \/        \/       \/         ''')
        ans = assets.utils.menu(["PLAY","EXIT","SETTINGS"])
        if ans == "PLAY":
            screens.char_creator()
    def char_creator():
        assets.characters.player.name = input("Player name: ")
        for i in range(5):
            print("Randomising stats \ ",end="\r")
            time.sleep(0.2)
            print("Randomising stats |",end="\r")
            time.sleep(0.2)
            print("Randomising stats / ",end="\r")
            time.sleep(0.2)
            print("Randomising stats - ",end="\r")
            time.sleep(0.2)
        assets.characters.player.create_random()
        assets.characters.player.printstats()
screens.home_screen()