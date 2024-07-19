import pygame
from Game.scripts.entities import Player, Enemy, BossEnemy
from Game.scripts.utils import load_image
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('DS3mini')

        self.clock = pygame.time.Clock()

        self.assets = {
            'background': load_image('map.png'),
            'boss_background': load_image('boss_map.png'),
        }

        self.level = 0
        self.level_defeated = {
            1: False,
            2: False,
            3: False,
            4: False
        }
        self.current_background = self.assets['background']

    def main(self):
        player = Player(self, 0, self.SCREEN_HEIGHT)
        self.enemies = pygame.sprite.Group()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not player.is_attacking:
                        player.melee_attack(self.enemies)

            player.update()

            collisions = pygame.sprite.spritecollide(player, self.enemies, False)
            for enemy in collisions:
                player.health -= 10

            if self.level == 1 and not self.level_defeated[1]:
                self.spawn_enemy(self.SCREEN_WIDTH // 4, self.SCREEN_HEIGHT - 160)
                self.level_defeated[1] = True
            elif self.level == 2 and not self.level_defeated[2]:
                self.spawn_enemy(self.SCREEN_WIDTH // 4, self.SCREEN_HEIGHT - 160)
                self.spawn_enemy(self.SCREEN_WIDTH * 3 // 4, self.SCREEN_HEIGHT - 160)
                self.level_defeated[2] = True
            elif self.level == 3 and not self.level_defeated[3]:
                self.spawn_enemy(self.SCREEN_WIDTH // 4, self.SCREEN_HEIGHT - 160)
                self.spawn_enemy(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT - 160)
                self.spawn_enemy(self.SCREEN_WIDTH * 3 // 4, self.SCREEN_HEIGHT - 160)
                self.level_defeated[3] = True
            elif self.level == 4 and not self.level_defeated[4]:
                self.current_background = self.assets['boss_background']
                self.spawn_enemy(self.SCREEN_WIDTH, self.SCREEN_HEIGHT - 320, is_boss=True)
                self.level_defeated[4] = True

            for enemy in self.enemies:
                enemy.update(player)

            self.screen.blit(self.current_background, (0, 0))
            player.draw_health_bar()
            self.enemies.draw(self.screen)
            self.screen.blit(player.image, player.rect)

            if player.is_attacking:
                attack_frame = player.attack_frames[player.current_frame]
                attack_rect = attack_frame.get_rect(midleft=player.rect.midright)
                self.screen.blit(attack_frame, attack_rect)

            for enemy in self.enemies:
                enemy.draw_health_bar()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def next_level(self):
        if len(self.enemies) == 0:
            self.level_defeated[self.level] = True
        self.level += 1
        if self.level > 4:
            self.level = 1
        print(f"Level: {self.level}")
        self.main()

    def spawn_enemy(self, x, y, is_boss=False):
        if is_boss:
            self.enemies.add(BossEnemy(self, x, y))
        else:
            self.enemies.add(Enemy(self, x, y))


if __name__ == "__main__":
    Game().main()
