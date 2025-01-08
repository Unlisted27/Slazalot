import os
import basicrpg
import assets
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
        assets.utils.menu(["PLAY","EXIT","SETTINGS"])
screens.home_screen()