from quantum_flappy_bird import QuantumFlappyBird
from quantum_ai import QuantumFlappyBirdAI
from quantum_multiplayer import QuantumMultiplayerFlappyBird
from quantum_weather import QuantumFlappyBirdWithWeather
from quantum_rewards import QuantumFlappyBirdWithRewards
from quantum_powerups import QuantumFlappyBirdWithPowerUps

def main():
    # Choose the game mode
    # Uncomment the mode you want to play

    # Basic Quantum Flappy Bird
    game = QuantumFlappyBird()

    # Quantum Flappy Bird with AI opponent
    # game = QuantumFlappyBirdAI()

    # Quantum Flappy Bird with Multiplayer mode
    # game = QuantumMultiplayerFlappyBird(num_players=2)

    # Quantum Flappy Bird with dynamic Quantum Weather
    # game = QuantumFlappyBirdWithWeather()

    # Quantum Flappy Bird with Quantum Rewards system
    # game = QuantumFlappyBirdWithRewards()

    # Quantum Flappy Bird with Quantum Power-Ups
    # game = QuantumFlappyBirdWithPowerUps()

    # Run the selected game mode
    game.game_loop()

if __name__ == "__main__":
    main()
