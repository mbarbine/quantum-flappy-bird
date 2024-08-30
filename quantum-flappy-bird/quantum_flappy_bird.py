import cudaq
import pygame
import sys
import cudaq

class QuantumBird:
    def __init__(self):
        self.y = 300
        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -10
        cudaq.set_target('density-matrix-cpu')
        self.noise = cudaq.NoiseModel()
        bit_flip_noise = cudaq.BitFlipChannel(0.1)
        self.noise.add_channel('x', [0], bit_flip_noise)
    
    def flap(self):
        self.velocity = self.flap_strength
        result = cudaq.sample(self.flap_kernel, noise_model=self.noise)
        bird_position = result.counts()
        if '0' in bird_position:
            self.velocity = 0
    
    @cudaq.kernel
    def flap_kernel(self):
        qubit = cudaq.qubit()
        h(qubit)
        mz(qubit)
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        if self.y < 0 or self.y > 600:
            self.y = 300
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (200, int(self.y)), 20)

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
