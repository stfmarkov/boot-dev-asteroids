from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def __move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
        
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        speed = self.velocity

        child_one = Asteroid(self.position.x, self.position.y, new_radius)
        child_two = Asteroid(self.position.x, self.position.y, new_radius)
        child_one.velocity = self.velocity.rotate(angle) * 1.2
        child_two.velocity = self.velocity.rotate(-angle) * 1.2

        self.kill()

    def update(self, dt):
        self.__move(dt)
