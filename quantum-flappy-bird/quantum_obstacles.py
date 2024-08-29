import cudaq

class QuantumObstacle:
    def __init__(self, position):
        self.position = position
        self.entangled_state = cudaq.qubit()

    @cudaq.kernel
    def entangle_with_bird(self, bird_position):
        cudaq.cx(bird_position, self.entangled_state)

    def check_collision(self, bird_position):
        self.entangle_with_bird(bird_position)
        obstacle_state = cudaq.measure(self.entangled_state)
        bird_state = cudaq.measure(bird_position)
        return bird_state == 1 and obstacle_state == 1
