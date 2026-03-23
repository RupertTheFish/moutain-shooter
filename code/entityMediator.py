from code.const import WINDOW_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
from code.playerShot import PlayerShot


# Most complex part of the code, relations between entities
class EntityMediator:
    # Collision with screen
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.heath = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WINDOW_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0


    # Shots, enemies
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_test = entity_list[i]
            EntityMediator.__verify_collision_window(entity_test)

    # Checking entity health parameter and removing
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)