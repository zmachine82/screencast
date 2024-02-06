import sys

import pygame
from pygame import KEYDOWN, K_ESCAPE


from ports.image_display_port import ImageDisplayPort


class PyGameImageDisplay(ImageDisplayPort):
    def __init__(self):
        pygame.init()

        self.ticks = pygame.time.get_ticks()
        self.prev_ticks = pygame.time.get_ticks()
        (self.width, self.height) = (1920, 1080)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.flip()

    def display_image(self, image):
        print(image)
        py_image = pygame.image.frombytes(image.tobytes(), image.size, image.mode)
        py_image = pygame.transform.scale(py_image, (self.width, self.height))
        self.screen.blit(py_image, (0, 0))
        pygame.display.flip()

        return pygame.time.get_ticks()

    def get_time(self):
        return pygame.time.get_ticks()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        self.clock.tick(60)
