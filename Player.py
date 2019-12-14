import pygame
import Colors


class Player(pygame.sprite.Sprite):
    #global life

    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()
        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(Colors.RED)
        self.rect = self.image.get_rect()
        self.life = 3

        self.speed_x = 0
        self.speed_y = 0

        self.level = None
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        # gravity / walls
        self.calc_grav()

        self.rect.x += self.speed_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.speed_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            elif self.speed_y < 0:
                self.rect.top = self.rect.bottom

            self.speed_y = 0

        if self.rect.y >= self.screen_height - 40:
            self.spawn()
            self.life -= 1

    def calc_grav(self):
        if self.speed_y == 0:
            self.speed_y = 1
        else:
            self.speed_y += .5
        if self.rect.y >= self.screen_height - self.rect.height and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = self.screen_height - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0:
            self.speed_y = -10
        # movement

    def left(self):
        self.speed_x = -6

    def right(self):
        self.speed_x = 6

    def stop(self):
        self.speed_x = 0

    def spawn(self):
        self.rect.x = 50
        self.rect.y = 500 - self.rect.height