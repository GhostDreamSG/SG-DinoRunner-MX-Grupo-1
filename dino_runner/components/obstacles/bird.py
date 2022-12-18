from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Bird(Obstacle):
    def __init__(self, image):

        self.type = 1
        super().__init__(image, self.type)