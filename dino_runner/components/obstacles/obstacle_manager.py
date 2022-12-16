import pygame
import random
from dino_runner.components.obstacles.captus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.index = 0

    def update(self, game_speed, game):
        for i in range(1):
            self.ram = [random.randint(0,1)]
            for ram in self.ram:
                self.index += 1
                if ram == 0:
                    if len(self.obstacles) == 0:
                        self.obstacles.append(Cactus(SMALL_CACTUS))
                else:
                    if len(self.obstacles) == 0:
                            self.obstacles.append(Bird(BIRD))           

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(300)
                game.playing = False
                break
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)