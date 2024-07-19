import pygame

from Game.scripts.utils import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.transform.scale(load_image('main_char.png'), (90, 160))
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.speed = 5
        self.health = 500
        self.max_health = 500
        self.health_bar_length = 100
        self.health_bar_height = 10

        self.attack_frames = [
            pygame.transform.scale(load_image(f'attack_{i}.png'), (90, 160)) for i in range(1, 3)
        ]
        self.current_frame = 0
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_cooldown = 10
        self.attack_range = 50

    def reset_position(self):
        self.rect.bottomleft = (0, self.game.SCREEN_HEIGHT)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not self.is_attacking:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and not self.is_attacking:
            self.rect.x += self.speed

        if self.rect.right > self.game.SCREEN_WIDTH:
            self.rect.left = 0
            self.game.next_level()

        if self.rect.left < 0:
            self.rect.left = 0

        if self.is_attacking:
            self.attack_timer += 1
            if self.attack_timer >= self.attack_cooldown:
                self.attack_timer = 0
                self.current_frame += 1
                if self.current_frame >= len(self.attack_frames):
                    self.is_attacking = False
                    self.image = pygame.transform.scale(load_image('main_char.png'), (90, 160))
                    self.current_frame = 0

    def draw_health_bar(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0),
                         (10, 10, self.health_bar_length, self.health_bar_height))
        current_health_bar_length = (self.health / self.max_health) * self.health_bar_length
        pygame.draw.rect(self.game.screen, (0, 255, 0),
                         (10, 10, current_health_bar_length, self.health_bar_height))

    def melee_attack(self, enemies):
        self.is_attacking = True
        self.attack_timer = 0
        self.current_frame = 0

        attack_rect = pygame.Rect(self.rect.right, self.rect.top, self.attack_range, self.rect.height)

        for enemy in enemies:
            if attack_rect.colliderect(enemy.rect):
                enemy.health -= 20
                if enemy.health <= 0:
                    enemy.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.transform.scale(load_image('enemy_1.png'), (90, 160))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.health = 50
        self.max_health = 50
        self.health_bar_length = 50
        self.health_bar_height = 5

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.game.SCREEN_WIDTH:
            self.rect.right = self.game.SCREEN_WIDTH

    def draw_health_bar(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0),
                         (self.rect.x, self.rect.y - 10, self.health_bar_length, self.health_bar_height))
        current_health_bar_length = (self.health / self.max_health) * self.health_bar_length
        pygame.draw.rect(self.game.screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, current_health_bar_length, self.health_bar_height))


class BossEnemy(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.transform.scale(load_image('boss.png'), (180, 320))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.health = 200
        self.max_health = 200
        self.health_bar_length = 200
        self.health_bar_height = 10

    def update(self, player):
        super().update(player)
