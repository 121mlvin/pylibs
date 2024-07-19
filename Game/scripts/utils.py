import pygame


def load_image(filename):
    filepath = f"images/{filename}"
    img = pygame.image.load(filepath).convert_alpha()
    return img
