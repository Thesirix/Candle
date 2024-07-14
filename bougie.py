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
            self.height -= self.speed / self.difficulty

        if self.height >= self.max_height * (self.difficulty / 10):
            self.difficulty += 1

        if self.height <= 0:
            self.height = 0

        self.y = HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Création de la bougie
bougie = Bougie()

# Variables du jeu
score = 0
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bougie.last_click_time = pygame.time.get_ticks()
            bougie.update()
            score += 1

    # Mise à jour de la bougie
    bougie.update()

    # Effacement de l'écran
    screen.fill(WHITE)

    # Affichage de la bougie
    bougie.draw()

    # Affichage du score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(score_text, (10, 10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limite de 60 images par seconde
    clock.tick(60)
    # voici exe final

# Fermeture de Pygame
pygame.quit()