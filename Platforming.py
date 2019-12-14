import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PASTEL_RED = (255, 105, 97)
MAGENTA_RED = (194, 30, 86)
TOMATO = (255,99,71)
SCARLET = (86, 3, 25)
PINK = (255, 105, 180)
BLUE = (0, 0, 255)
LIME_GREEN = (50, 205, 50)
SKY_BLUE = (135, 206, 235)
TURQUOISE = (175, 238, 238)

screen_width = 800
screen_height = 600

done = False

class Player(pygame.sprite.Sprite):
    global life
    def __init__(self):
        super(Player, self).__init__()
        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.life = 3

        self.speed_x = 0
        self.speed_y = 0

        self.level = None

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

        if self.rect.y >= screen_height - 40:
            self.spawn()
            self.life -= 1

    def calc_grav(self):
        if self.speed_y == 0:
            self.speed_y = 1
        else:
            self.speed_y += .5
        if self.rect.y >= screen_height - self.rect.height and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = screen_height - self.rect.height

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

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Platform, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
# levels


class Level(object):
    def __init__(self, player):

        self.platform_list = pygame.sprite.Group()
        self.player = player

        self.background = None

        self.world_shift = 0
      # updates when called

    def update_lvl(self):
        self.platform_list.update()
    def draw(self, screen):

        screen.fill(BLACK)
        self.platform_list.draw(screen)

class Level_1(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.level_limit = -1000

        # width, height ,x, y of plat
        level = [[400, 100, 0, 500],
                 [5, 100, 500, 500],
                 [5, 460, 500, 0],
                [300, 100, 600, 500]]
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.player = self.player
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)

class Level_2(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.level_limit = -1000

        level = [[200, 100, 0, 500],
                 [400, 100, 300, 500]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.player = self.player
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)

class Level_3(Level):
    def __init__(self,player):
        Level.__init__(self,player)
        self.level_limit = -1000

        level = [[100, 100, 0, 500],
                 [300, 100, 200, 500],
                 [200, 100, 600, 500]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.player = self.player
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)


class Level_4(Level):
    def __init__(self,player):
        Level.__init__(self,player)
        self.level_limit = -1000

        level = [[400, 100, 0, 500],
                 [30, 30, 450, 400],
                 [30, 30, 600, 350],
                 [100, 100, 700, 500]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.player = self.player
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)

class Level_5(Level):
    def __init__(self,player):
        Level.__init__(self,player)
        self.level_limit = -1000

        level = [[50, 50, 50, 500],
                 [40, 40, 190, 400],
                 [50, 50, 330, 500],
                 [40, 40, 480, 480],
                 [60, 50, 680, 400]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.player = self.player
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)

class Level_6(Level):
    def __init__(self,player):
        Level.__init__(self,player)
        self.level_limit = -1000

        level = [[100, 100, 0, 500],
                 [20, 20, 200, 400],
                 [10, 10, 350, 300],
                 [5, 5, 430, 200],
                 [100, 100, 700, 500]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.player = self.player
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)

player = Player()

lvl_list = []
lvl_list.append(Level_1(player))
lvl_list.append(Level_2(player))
lvl_list.append(Level_3(player))
lvl_list.append(Level_4(player))
lvl_list.append(Level_5(player))
lvl_list.append(Level_6(player))

current_lvl_num = 0
death_zone = 800

class Game:
    def __init__(self):
        self.on_screen = 0

    def init(self):
        pygame.init()

        self.size = [screen_width, screen_height]
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("The Floor Isn't Lava ATM")

    def screen_1(self):
        self.screen.fill(GREEN)

        self.screen.blit()

    def main_loop(self):
        self.init()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.on_screen = 1

                if self.on_screen == 1:
                    self.screen_1()

game = Game()
game.main_loop()








# def main():
#     # main program
#     pygame.init()
#
#     size = [screen_width, screen_height]
#     screen = pygame.display.set_mode(size)
#
#     pygame.display.set_caption("The Floor Isn't Lava ATM")
#
#     clock = pygame.time.Clock()
#
#     font = pygame.font.SysFont("TimeNewRoman", 40)
#     title_text_font = pygame.font.SysFont("TimeNewRoman", 100)
#     start_text_font = pygame.font.SysFont("TimeNewRoman", 75)
#     lvl_select_text_font = pygame.font.SysFont("TimeNewRoman", 75)
#     back_text_font = pygame.font.SysFont("TimeNewRoman", 50)
#     lvl_text_font = pygame.font.SysFont("TimesNewRoman", 40)
#     game_over_text_font = pygame.font.SysFont("TimesNewRoman", 100)
#
#     # Main Program
#     def game_menu():
#         menu_done = False
#         global done
#         global current_lvl_num
#         while not menu_done:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     done = True
#                     menu_done = True
#
#             screen.fill(BLACK)
#
#             title_text = title_text_font.render("The Floor Is Lava!", True, WHITE)
#             title_text_rect = title_text.get_rect()
#             title_text_rect.centerx = 400
#             title_text_rect.centery = 100
#             # x, y, width, height
#
#             mouse = pygame.mouse.get_pos()
#
#             if 600 > mouse[0] > 200 and 300 > mouse[1] > 200:
#                 pygame.draw.rect(screen, GREEN, (200, 200, 400, 100))
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     menu_done = True
#                     current_lvl_num = 0
#                     game_loop()
# # x, y, width, height
#             else:
#                 pygame.draw.rect(screen, LIME_GREEN, (200, 200, 400, 100))
#
#             start_text = start_text_font.render("START!", True, WHITE)
#             start_text_rect = start_text.get_rect()
#             start_text_rect.centerx = 400
#             start_text_rect.centery = 250
#
#             if 600 > mouse[0] > 200 and 500 > mouse[1] > 400:
#                 pygame.draw.rect(screen, PINK, (200, 400, 400, 100))
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     menu_done = True
#                     lvl_select_loop()
#
#
#             else:
#                 pygame.draw.rect(screen, MAGENTA_RED, (200, 400, 400, 100))
#
#             lvl_select_text = lvl_select_text_font.render("LEVEL SELECT", True, WHITE)
#             lvl_select_text_rect = lvl_select_text.get_rect()
#             lvl_select_text_rect.centerx = 400
#             lvl_select_text_rect.centery = 450
#
#             if menu_done == False:
#                 screen.blit(title_text, title_text_rect)
#                 screen.blit(start_text, start_text_rect)
#                 screen.blit(lvl_select_text, lvl_select_text_rect)
#
#             clock.tick(60)
#
#             pygame.display.flip()
#
#
#     def lvl_select_loop():
#
#         lvl_select_done = False
#         global done
#         global lvl_list
#         global current_lvl_num
#
#         button_width = 200
#         button_height = 200
#
#         while not lvl_select_done:
#             mouse_down = False
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     done = True
#                     lvl_select_done = True
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     mouse_down = True
#
#             screen.fill(BLACK)
#
#             mouse = pygame.mouse.get_pos()
#
#             lvl_count = 0
#
#             for level in lvl_list:
#                 button_y = 20 + lvl_count*60
#
#                 if 500 > mouse[0] > 200 and 50+button_y > mouse[1] > button_y:
#                     pygame.draw.rect(screen, TURQUOISE, (100, button_y, 400, 50))
#                     if mouse_down == True:
#                         lvl_select_done = True
#                         current_lvl_num = lvl_count
#                         game_loop()
#
#                         # x, y, width, height
#                 else:
#                     pygame.draw.rect(screen, SCARLET, (100, button_y, 400, 50))
#
#                 lvl_text = lvl_text_font.render("Level "+str(lvl_count+1), True, WHITE)
#                 lvl_text_rect = lvl_text.get_rect()
#                 lvl_text_rect.centerx = 300
#                 lvl_text_rect.centery = (60*lvl_count)+40
#
#                 lvl_count += 1
#                 screen.blit(lvl_text, lvl_text_rect)
#
#             if 750 > mouse[0] > 600 and 550 > mouse[1] > 500:
#                 pygame.draw.rect(screen, PASTEL_RED, (600, 500, 150, 50))
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     lvl_select_done = True
#                     game_menu()
#
#                     # to calc center x & y, width or  height / 2 + x or y
#             else:
#                 pygame.draw.rect(screen, SCARLET, (600, 500, 150, 50))
#
#             back_text = back_text_font.render("Back", True, WHITE)
#             back_text_rect = back_text.get_rect()
#             back_text_rect.centerx = 675
#             back_text_rect.centery = 525
#
#             if lvl_select_done == False:
#                 screen.blit(back_text, back_text_rect)
#                 clock.tick(60)
#                 pygame.display.flip()
#
#     def game_over_screen():
#         game_over_done = False
#
#         global life
#         global done
#         global current_lvl_num
#
#         while not game_over_done:
#             mouse_click = 0
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     done = True
#                     game_over_done = True
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     mouse_click = 1
#
#             mouse = pygame.mouse.get_pos()
#             click = pygame.mouse.get_pressed()
#
#             screen.fill(BLACK)
#
#             if 550 > mouse[0] > 250 and 430 > mouse[1] > 380:
#                 pygame.draw.rect(screen, GREEN, (250, 380, 300, 50))
#                 if mouse_click == 1:
#                     game_over_done = True
#                     player.life = 3
#                     main()
#
#                     # x, y, width, height
#             else:
#                 pygame.draw.rect(screen, LIME_GREEN, (250, 380, 300, 50))
#
#             game_over_text = game_over_text_font.render("Game Over!", True, RED)
#             game_over_text_rect = game_over_text.get_rect()
#             game_over_text_rect.centerx = 400
#             game_over_text_rect.centery = 300
#
#             click_spawn_text = font.render("Try Again?", True, PASTEL_RED)
#             click_spawn_text_rect = click_spawn_text.get_rect()
#             click_spawn_text_rect.centerx = 400
#             click_spawn_text_rect.centery = 405
#
#             if game_over_done == False:
#                 screen.blit(game_over_text, game_over_text_rect)
#                 screen.blit(click_spawn_text, click_spawn_text_rect)
#                 clock.tick(60)
#                 pygame.display.flip()
#
#     def game_loop():
#         global done
#         global current_lvl_num
#         global death_zone
#
#         current_lvl = lvl_list[current_lvl_num]
#         active_sprite_list = pygame.sprite.Group()
#         player.level = current_lvl
#
#         player.spawn()
#         active_sprite_list.add(player)
#
#         while not done:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     done = True
#
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         player.left()
#                     if event.key == pygame.K_RIGHT:
#                         player.right()
#                     if event.key == pygame.K_UP:
#                         player.jump()
#                     if event.key == pygame.K_ESCAPE:
#                         game_menu()
#
#                 if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_LEFT and player.speed_x < 0:
#                         player.stop()
#                     if event.key == pygame.K_RIGHT and player.speed_x > 0:
#                         player.stop()
#
#             active_sprite_list.update()
#             current_lvl.update_lvl()
#
#             if player.rect.left < 0:
#                 player.rect.left = 0
#
#             if player.life == 0:
#                 game_over_screen()
#
#                 # If the player gets to the end of the level, go to the next level
#             if player.rect.x >= death_zone:
#                 player.spawn()
#                 if current_lvl_num < len(lvl_list) - 1:
#                     current_lvl_num += 1
#                     current_lvl = lvl_list[current_lvl_num]
#                     player.level = current_lvl
#
#             if player.rect.x <= 0 and current_lvl_num > 0:
#                 player.spawn()
#                 if current_lvl_num < len(lvl_list) + 1:
#                     current_lvl_num -= 1
#                     current_lvl = lvl_list[current_lvl_num]
#                     player.level = current_lvl
#
#             # drawing code
#
#             current_lvl.draw(screen)
#             active_sprite_list.draw(screen)
#
#             lvl_text = font.render("Level: " + str(current_lvl_num+1), True, WHITE)
#             lvl_text_rect = lvl_text.get_rect()
#             lvl_text_rect.centerx = 400
#             lvl_text_rect.centery = 50
#
#             life_text = font.render("Lives: " + str(player.life), True, WHITE)
#             life_text_rect = life_text.get_rect()
#             life_text_rect.centerx = 400
#             life_text_rect.centery = 100
#
#             screen.blit(lvl_text, lvl_text_rect)
#             screen.blit(life_text, life_text_rect)
#
#             clock.tick(60)
#
#             pygame.display.flip()
#
#     game_menu()
#     pygame.quit()

if __name__ == "__main__":
    main()














