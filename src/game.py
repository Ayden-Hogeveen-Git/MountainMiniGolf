from colours import Colours
from button import Button
from math import atan2, cos, sin
import pygame
pygame.init()


class Game:
    def __init__(self) -> None:
        # Windows
        self.running = True
        self.width, self.height = 1080, 640
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        # Scene
        self.scene = 0
        
        # Colours and Fonts
        self.colours = Colours()
        self.title_font = pygame.font.Font('freesansbold.ttf', 64)
        self.h1_font = pygame.font.Font('freesansbold.ttf', 32)

        # Buttons
        self.start_button = Button(self.width // 2 - 100, self.height // 2 - 50, 200, 100, text="Start", color=self.colours.DARK_GRASS_GREEN, hover_color=self.colours.GREEN)

        self.buffer = 25

        # Game Variables
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0


    def draw_start_screen(self):
        title = self.title_font.render("Mountain Mini Golf", True, self.colours.BLACK)
        title_rect = title.get_rect(center=(self.width // 2, self.height // 4))

        start_text = self.h1_font.render("Start", True, self.colours.BLACK)
        start_rect = start_text.get_rect(center=(self.width // 2, self.height // 2))

        self.start_button.draw(self.screen, self.colours.WOOD_BROWN)

        self.screen.blit(title, title_rect)

    def draw(self):
        pygame.draw.rect(self.screen, self.colours.WOOD_BROWN, (0, 0, self.width, self.height))
        pygame.draw.rect(self.screen, self.colours.LIGHT_GRASS_GREEN, (self.buffer, self.buffer, self.width - self.buffer * 2, self.height - self.buffer * 2))

        # Title Screen
        if (self.scene == 0):
            self.draw_start_screen()

    def track_mouse(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        print(f"X: {self.mouse_x}, Y: {self.mouse_y}")
        return self.mouse_x, self.mouse_y

    def calc_shot(self, x1, y1, x2, y2):
        dX, dY = x2 - x1, y2 - y1
        return atan2(dY, dX)

    ###
    def move_circle(self, ball_x, ball_y, target_x, target_y, speed):
        angle = self.calc_shot(ball_x, ball_y, target_x, target_y)
        direction_x = cos(angle)
        direction_y = sin(angle)
        ball_x += direction_x * speed
        ball_y += direction_y * speed
        return ball_x, ball_y
    ###
    
    def run(self):
        while (self.running):
            self.screen.fill((0, 0, 0))

            self.draw()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.running = False

                # Mouse Click Actions
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (self.scene == 0):
                        if (self.start_button.is_over(pygame.mouse.get_pos())):
                            self.scene = 1

                    if (self.scene != 0):
                        self.x1, self.y1 = self.track_mouse()

                if (event.type == pygame.MOUSEBUTTONUP):
                    if (self.scene != 0):
                        self.x2, self.y2 = self.track_mouse()
                        angle = self.calc_shot(self.x1, self.y1, self.x2, self.y2)
                        print(angle)

                # Button Actions
                if (event.type == pygame.MOUSEMOTION):
                    if (self.start_button.is_over(pygame.mouse.get_pos())):
                        self.start_button.color = self.start_button.hover_color
                    else:
                        self.start_button.color = self.colours.DARK_GRASS_GREEN
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
        quit()
