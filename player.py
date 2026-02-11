import pygame
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS
)
from circleshape import CircleShape
from shot import Shot


#player class to define hitbox and graphic
class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        

    #defines the triangle and it's hitbox
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
   #logic for shooting
    def shoot(self):
        if self.shoot_timer > 0:
            return 
        
        velocity = (
            pygame.Vector2(0, 1)
            .rotate(self.rotation)
            * PLAYER_SHOOT_SPEED
        )

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS


    #movement key logic + update for shoot()
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector