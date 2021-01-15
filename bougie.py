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
