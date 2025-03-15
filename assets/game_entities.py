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
def tester():
    print(input("TESTING! "))
class rooms:
    def __init__(self):
        pass
    dungeon_enterance = basicrpg.room("Dungeon entrance","You are at the entrance to a dungeon. There is a door to the north leading inside",tester)
    dungeon_intersection_1 = basicrpg.room("First dungeon intersection","You stand in a small stone room. There is a door to the south leading outside, there is a path to the north leading down a dark hallway, and a path to the west, leading to a large, dark chamber.")
    dungeon_dining_chamber = basicrpg.room("Large dining chamber","You are in a vast dining hall. Rotten benches and tables are in rows leading to the front of the room where a long table stands on an elevated platform. There is a door to the east leading to the entrance intersection, and a door to the north near the long table at the front.")
    dungeon_hallway_1 = basicrpg.room("Hallway","You are in a long hallway. Stone runes line the walls. There is a door to the south leading to the entrance intersection, a door to the west, and a chamber to the north.")
    dungeon_kitchen = basicrpg.room("Kitchen","You are in a ruined kitchen. The smell of rot fills the air. There is a door to the east, and a door to the south.")
    dungeon_final_chamber = basicrpg.room("End chamber","You are in a cramped chamber. Chests and piles of gold line the walls, and a throne sits in the middle. There is a door to the south leading to a hallway")

    dungeon_enterance.set_doors({"North":dungeon_intersection_1})
    dungeon_intersection_1.set_doors({"South":dungeon_enterance,"West":dungeon_dining_chamber,"North":dungeon_hallway_1})
    dungeon_dining_chamber.set_doors({"North":dungeon_kitchen,"East":dungeon_intersection_1})
    dungeon_hallway_1.set_doors({"South":dungeon_intersection_1,"West":dungeon_kitchen,"North":dungeon_final_chamber})
    dungeon_kitchen.set_doors({"South":dungeon_dining_chamber,"East":dungeon_hallway_1})
    dungeon_final_chamber.set_doors({"South":dungeon_hallway_1})