# Ball Game
### Developed by Malki Applebaum ✍️

## Description
Ball Game is an interactive 2-player arcade game where two players control paddles to bounce a ball back and forth. The goal of the game is to prevent the ball from going past your paddle while trying to make the ball go past your opponent's paddle.

The game features two walls, which are controlled by the players using the keyboard. The players can move their walls in the game to block the ball and score points. The game ends when the player quits the game by pressing the `q` key.

![Game Screenshot](screenshot%20ball%20game.png)

## How to Play
1. **Player 1** uses the **WASD** keys to move the left wall.
   - **W** to move up
   - **A** to move left
   - **S** to move down
   - **D** to move right

2. **Player 2** uses the **Numpad keys (8, 4, 6, 2)** to move the right wall.
   - **8** to move up
   - **2** to move down
   - **4** to move left
   - **6** to move right

3. The ball moves continuously and bounces off the walls. If the ball hits the left side of the screen, **Player 2** gets a point. If the ball hits the right side of the screen, **Player 1** gets a point.

4. You can also control the speed of the balls by pressing:
   - **U** to increase speed
   - **L** to decrease speed
   - **I** to reverse the direction of the ball

5. The game continues until you press the `q` key to quit.

## Requirements
- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MalkiApplebaum/Ball-in-Python.git
