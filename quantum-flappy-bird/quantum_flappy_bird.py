import cudaq
import pygame
import sys

# Initialize the game engine
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Flappy Bird")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Bird properties
bird_x, bird_y = 100, height // 2
bird_size = 20

# Game loop flag
running = True

# Quantum properties
bird_position = cudaq.qubit()

@cudaq.kernel
def quantum_flap():
    cudaq.h(bird_position)
    position = cudaq.measure(bird_position)
    return position

def game_loop():
    global bird_y
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Trigger quantum flap
                    position = quantum_flap()
                    if position == 1:
                        bird_y -= 50  # Move up
                    else:
                        bird_y += 10  # Slightly move down or stay

        bird_y += 5  # Gravity effect

        # Draw background
        window.fill(white)

        # Draw bird
        pygame.draw.rect(window, black, [bird_x, bird_y, bird_size, bird_size])

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
