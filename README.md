# Tic-Tac-Toe AI

An unbeatable Tic-Tac-Toe game using the Minimax algorithm with Alpha-Beta Pruning.

## Features
- Human vs AI gameplay.
- AI uses the Minimax algorithm to ensure it never loses.
- Alpha-Beta Pruning for optimized search performance.
- Simple Command-Line Interface (CLI).

## Project Structure
- `tic_tac_toe.py`: Main game loop and CLI.
- `minimax.py`: Implementation of the Minimax algorithm.

## How to Run
1. Ensure you have Python installed.
2. Run the following command:
   ```bash
   python tic_tac_toe.py
   ```

## Rules
- The human player is 'X' and moves first.
- The AI is 'O'.
- Players take turns placing their marks in empty squares (1-9).
- The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins.
- If all 9 squares are full and no player has 3 marks in a row, the game is a draw.
