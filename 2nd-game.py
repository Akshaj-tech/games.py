import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Game')

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
PLAYER_SIZE = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * PLAYER_SIZE]
PLAYER_SPEED = 10

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Properly exit the loop

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
        player_pos[0] += PLAYER_SPEED

    # Drawing the game screen
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.display.flip()

    # Limit FPS
    clock.tick(30)

pygame.quit()
sys.exit()