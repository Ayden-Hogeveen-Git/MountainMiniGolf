import pygame


class Button:
    def __init__(self, x, y, width, height, text=None, color=(73, 73, 73), hover_color=(189, 189, 189), font_name='freesansbold.ttf', font_size=32):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(font_name, font_size)

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, outline=None):
        if (outline):
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if (self.text):
            text = self.font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        return self.rect.collidepoint(pos)