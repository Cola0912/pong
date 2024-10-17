
# Pong Game with Socket Communication

This is a simple Pong game implemented in Python using Pygame, with support for two players over a network using socket communication. One PC acts as the server, and another PC acts as the client. The server controls player 1, while the client controls player 2.

## Requirements

- Python 3.x
- Pygame
- Socket module (comes with Python)

## Installation

1. Install Pygame if you haven't already:

   ```bash
   pip install pygame
   ```

2. Download the server and client Python scripts.

## How to Run

### 1. Server (Player 1)

Run the server on one PC. This will allow you to control Player 1 using the `W` and `S` keys.

```bash
python server.py
```

### 2. Client (Player 2)

On the second PC, run the client to connect to the server. You will need to enter the server's IP address. Player 2 can be controlled using the arrow keys.

```bash
python client.py
```

### Game Controls

- **Player 1 (Server)**: Use `W` (up) and `S` (down) keys to move the paddle.
- **Player 2 (Client)**: Use the arrow keys to move the paddle.

### Winning Condition

The first player to reach 10 points wins the game. Once a player wins, the game will display the winner and automatically close after 3 seconds.

## License

This project is open-source and free to use under the MIT License.
