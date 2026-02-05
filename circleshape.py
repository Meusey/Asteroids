from constants import LINE_WIDTH
import pygame

#base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(*self.containers)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
