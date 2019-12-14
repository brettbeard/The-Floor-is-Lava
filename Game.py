import pygame
import Colors
from Player import Player

screen_width = 800
screen_height = 600

MAIN_MENU = 0
GAME_LOOP = 1
LEVEL_SELECT = 2

class Game:

    def __init__(self):
        self.screen_number = MAIN_MENU

        self.screen = None
        self.clock = None

        self.title_text_font = None
        self.font = None
        self.start_text_font = None
        self.lvl_select_text_font = None
        self.back_text_font = None
        self.lvl_text_font = None
        self.game_over_text_font = None

        self.lvl_list = [0,1]

    def initialize(self):
        pygame.init()

        size = [screen_width, screen_height]
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("The Floor Isn't Lava ATM")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("TimeNewRoman", 40)
        self.title_text_font = pygame.font.SysFont("TimeNewRoman", 100)
        self.start_text_font = pygame.font.SysFont("TimeNewRoman", 75)
        self.lvl_select_text_font = pygame.font.SysFont("TimeNewRoman", 75)
        self.back_text_font = pygame.font.SysFont("TimeNewRoman", 50)
        self.lvl_text_font = pygame.font.SysFont("TimesNewRoman", 40)
        self.game_over_text_font = pygame.font.SysFont("TimesNewRoman", 100)

    def shutdown(self):
        pygame.quit()

    def main_menu(self):

        title_text = self.title_text_font.render("The Floor Is Lava!", True, Colors.WHITE)
        title_text_rect = title_text.get_rect()
        title_text_rect.centerx = 400
        title_text_rect.centery = 100
        # x, y, width, height

        start_text = self.start_text_font.render("START!", True, Colors.WHITE)
        start_text_rect = start_text.get_rect()
        start_text_rect.centerx = 400
        start_text_rect.centery = 250

        lvl_select_text = self.lvl_select_text_font.render("LEVEL SELECT", True, Colors.WHITE)
        lvl_select_text_rect = lvl_select_text.get_rect()
        lvl_select_text_rect.centerx = 400
        lvl_select_text_rect.centery = 450

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.screen_number = -1

            mouse = pygame.mouse.get_pos()

            self.screen.fill(Colors.BLACK)

            if 600 > mouse[0] > 200 and 300 > mouse[1] > 200:
                pygame.draw.rect(self.screen, Colors.GREEN, (200, 200, 400, 100))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Go to game loop
                    self.screen_number = GAME_LOOP
                    done = True
            # x, y, width, height
            else:
                pygame.draw.rect(self.screen, Colors.LIME_GREEN, (200, 200, 400, 100))

            if 600 > mouse[0] > 200 and 500 > mouse[1] > 400:
                pygame.draw.rect(self.screen, Colors.PINK, (200, 400, 400, 100))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Go to level select
                    self.screen_number = LEVEL_SELECT
                    done = True
            else:
                pygame.draw.rect(self.screen, Colors.MAGENTA_RED, (200, 400, 400, 100))

            self.screen.blit(title_text, title_text_rect)
            self.screen.blit(start_text, start_text_rect)
            self.screen.blit(lvl_select_text, lvl_select_text_rect)

            self.clock.tick(60)

            pygame.display.flip()

    def level_select(self):
        back_text = self.back_text_font.render("Back", True, Colors.WHITE)
        back_text_rect = back_text.get_rect()
        back_text_rect.centerx = 675
        back_text_rect.centery = 525

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.screen_number = -1

            mouse = pygame.mouse.get_pos()

            self.screen.fill(Colors.BLACK)

            lvl_count = 0

            for level in self.lvl_list:
                button_y = 20 + lvl_count * 60

            if 750 > mouse[0] > 600 and 550 > mouse[1] > 500:
                pygame.draw.rect(self.screen, Colors.PASTEL_RED, (600, 500, 150, 50))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done = True
                    self.screen_number = MAIN_MENU

                    # to calc center x & y, width or  height / 2 + x or y
            else:
                pygame.draw.rect(self.screen, Colors.SCARLET, (600, 500, 150, 50))

            self.screen.blit(back_text, back_text_rect)

            self.clock.tick(60)

            pygame.display.flip()

    def game_loop(self):
        player = Player(screen_width, screen_height)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.screen_number = -1

            mouse = pygame.mouse.get_pos()

            self.screen.fill(Colors.BLACK)

            self.clock.tick(60)
            pygame.display.flip()

    def main_loop(self):

        self.initialize()

        done = False
        while not done:
            if self.screen_number == MAIN_MENU:
                self.main_menu()
            elif self.screen_number == GAME_LOOP:
                self.game_loop()
            elif self.screen_number == LEVEL_SELECT:
                self.level_select()
            elif self.screen_number == -1:
                done = True

        self.shutdown()