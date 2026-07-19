# TicTacToe

Tic-Tac-Toe AI — Minimax Algorithm

A Python implementation of Tic-Tac-Toe where the AI opponent uses the Minimax algorithm as described in Russell & Norvig's Artificial Intelligence: A Modern Approach (Figure 5.3). Built with a graphical interface using Python's built-in tkinter library.

## Features

Human (X) vs AI (O) gameplay
Unbeatable AI powered by Minimax
Clean GUI with game status updates
Winning cells highlighted in green
Restart button to play again

## How It Works

The AI uses the Minimax algorithm — a recursive decision-making technique from game theory. It simulates every possible future move, builds a complete game tree, and picks the move that leads to the best outcome assuming the opponent also plays optimally.

## Requirements

Python 3.x
No external libraries needed (tkinter is included with Python)

## How to Run

```bash
python tictactoe.py
```

The game window will open. Click any cell to play as X. The AI responds as O.

## Project Structure

tictactoe.py
│
├── check_winner(board) # Detects if X or O has won
├── is_draw(board) # Checks if board is full with no winner
├── terminal_test(board) # Combines winner + draw check
├── utility(board, depth) # Returns score for terminal state
├── max_value(board, depth) # Minimax MAX-VALUE (AI's turn)
├── min_value(board, depth) # Minimax MIN-VALUE (Human's turn)
├── best_move(board) # MINIMAX-DECISION — picks best move
└── class TicTacToe # tkinter GUI (buttons, labels, restart)

## Why the AI is Unbeatable

Minimax explores the complete game tree every possible sequence of moves from the current state to the end. Since Tic-Tac-Toe has at most 9! = 362,880 possible game states, this is computationally feasible. The AI assumes you always play optimally, so it never relies on you making a mistake. The best outcome you can force is a draw.

## Reference

Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Figure 5.3 — Minimax Decision Algorithm.
