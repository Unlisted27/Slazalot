import basicrpg
class races:
    human = basicrpg.race("Human",0,0,0,0)
    goblin = basicrpg.race("Goblin",-1,-1,-1,0)
class professions:
    commoner = basicrpg.profession("Commoner")

class items:
    class weapons:
        def __init__(self):
            pass
        sword = basicrpg.weapon("Long Sword",3,"A fine blade stretching from a hardwood handguard",(1,8),0)
        mase = basicrpg.weapon("Mase",4,"A heavy, metal hammer",(1,6),0)
        battleaxe = basicrpg.weapon("Battleaxe",4,"A sturdy blade, used to cut more than wood",(1,8),0)