import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Line:
    def __init__(self, line, background, to_postrender = True):
        self.line = line
        self.background = background
        self.to_postrender = to_postrender

