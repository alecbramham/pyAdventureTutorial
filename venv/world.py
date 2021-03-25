import items
import enemies
import random


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a Subclass instead!")

    def modify_player(self, player):
        pass


class StartingRoom(MapTile):
    def intro_text(self):
        return '''You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.'''

    def modify_player(self, player):
        # Room has no action on player
        pass


class VictoryTile(MapTile):
    def intro_text(self):
        return '''You see a dim light in the distance. It grows brighter as you approach it. It's sunlight!
        Victory is yours!'''


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = 'A giant spider jumps down from its web in front of you!'
            self.dead_text = 'The corpse of a dead spider rots on the ground.'
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = 'A giant ogre is blocking your path!'
            self.dead_text = 'A dead ogre reminds you of your victory.'
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = 'You hear a squeaking noise growing louder ... suddenly you are lost in a swarm of bats'
            self.dead_text = 'Dozens of dead bats are scattered on the ground.'
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "You've disturbed a rock monster from his slumber!"
            self.dead_text = 'Defeated, the monster has reverted into an ordinary rock.'
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text
        else:
            text = self.dead_text
        return text

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print('Enemy does {} damage. You have {} HP remaining.'.format(self.enemy.damage, the_player.hp))


class EmptyCavePath(MapTile):
    def intro_text(self):
        return 'Another unremarkable part of the cave. You must forge onwards.'

    def modify_player(self, player):
        # Room has no action on player
        pass


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return "You notice something vaguely shiny in the corner of the room. It's a dagger! You pick it up."


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return 'You find a small pouch with 5 gold coins in it. The coins jingle as you pick up the pouch.'


class FindCrustyBreadRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.CrustyBread())

    def intro_text(self):
        return 'There is a small parcel on the ground. Inside is a small loaf of hard, crusty bread. You pick it up.'


world_map = [
    [None, VictoryTile(1, 0), EnemyRoom(2, 0)],
    [StartingRoom(0, 1), None, Find5GoldRoom(2, 1)],
    [EnemyRoom(0, 2), FindCrustyBreadRoom(1, 2), EnemyRoom(2, 2)],
    [FindDaggerRoom(0, 3), None, EnemyRoom(2, 3)],
]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
