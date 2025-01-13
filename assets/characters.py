import basicrpg
from assets import game_entities

player = basicrpg.character(game_entities.races.human,game_entities.professions.commoner,"DEFAULT")

companion = basicrpg.character(game_entities.races.human,game_entities.professions.commoner,basicrpg.genname())

goblin = basicrpg.character(game_entities.races.human,game_entities.professions.commoner,basicrpg.genname())