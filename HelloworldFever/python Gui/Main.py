import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smoke Effect Hello World")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Smoke particles
smoke_particles = []

# Create a font object
font = pygame.font.Font(None, 64)

# Text
text = font.render("Hello, World!", True, WHITE)

def create_smoke_particle():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    size = random.randint(10, 30)
    color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255), random.randint(50, 200))
    return [x, y, size, color]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Create and update smoke particles
    if random.randint(1, 10) > 6:
        smoke_particles.append(create_smoke_particle())
    for particle in smoke_particles:
        particle[1] -= 1
        particle[2] -= 0.2
        if particle[2] <= 0:
            smoke_particles.remove(particle)
    for particle in smoke_particles:
        pygame.draw.circle(screen, particle[3], (int(particle[0]), int(particle[1])), int(particle[2]))

    # Render the "Hello, World!" text
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()