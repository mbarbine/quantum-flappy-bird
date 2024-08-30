import cudaq
from quantum_flappy_bird import QuantumFlappyBird
import pygame
import numpy as np

class QuantumWeather:
    def __init__(self):
        self.wind = 0
    
    def update(self, bird):
        self.wind = np.random.uniform(-1, 1)
        bird.velocity += self.wind
    
    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        wind_text = font.render(f"Wind: {self.wind:.2f}", True, (0, 0, 0))
        screen.blit(wind_text, (10, 50))
class QuantumWeather:
    def __init__(self):
        self.weather_state = cudaq.qubit()

    @cudaq.kernel
    def change_weather(self):
        cudaq.h(self.weather_state)
        current_weather = cudaq.measure(self.weather_state)
        return current_weather

    def apply_weather_effect(self, bird_y):
        weather_effect = self.change_weather()
        if weather_effect == 1:
            bird_y += 20
        return bird_y
    
    def update(self, bird):
        self.wind = np.random.uniform(-1, 1) * bird.bloch_vector[2]  # Wind depends on Z component of Bloch vector
        bird.velocity += self.wind
    
    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        wind_text = font.render(f"Wind: {self.wind:.2f}", True, (0, 0, 0))
        screen.blit(wind_text, (10, 50))

class QuantumFlappyBirdWithWeather(QuantumFlappyBird):
    def __init__(self):
        super().__init__()
        self.weather_system = QuantumWeather()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        position = self.quantum_flap()
                        if position == 1:
                            self.bird_y -= 50
                        else:
                            self.bird_y += 10

            self.bird_y = self.weather_system.apply_weather_effect(self.bird_y)
            self.window.fill((255, 255, 255))
            pygame.draw.rect(self.window, (0, 0, 0), [self.bird_x, self.bird_y, self.bird_size, self.bird_size])
            pygame.display.update()
            self.clock.tick(30)
