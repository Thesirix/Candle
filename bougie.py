import pygame

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
WIDTH = 800
HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la bougie japonaise")

clock = pygame.time.Clock()

# Classe représentant la bougie japonaise
class Bougie:
    def __init__(self):
        self.width = 50
        self.height = 0
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height
        self.speed = 1
        self.max_height = HEIGHT - 50
        self.difficulty = 1
        self.last_click_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        time_since_last_click = current_time - self.last_click_time

        if time_since_last_click <= 100:
            self.height += self.speed
        else:
