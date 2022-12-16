import random
from dino_runner.components.obstacles.obstacle import Obstacle
class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        for i in range(1):
            self.ran = [random.randint(0,1)]
            for ran in self.ran:
                if ran % 2 == 0:
                    self.rect.y = 325
                else: 
                    self.rect.y = 250