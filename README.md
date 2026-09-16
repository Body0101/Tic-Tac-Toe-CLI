# Tic Tac Toe (CLI)

A simple two-player Tic Tac Toe game that runs in the terminal, built with Python. Uses [`rich`](https://github.com/Textualize/rich) for colorful, styled terminal output and [`pyfiglet`](https://github.com/pwaller/pyfiglet) for the ASCII-art win banner.

## Features

- Local two-player gameplay
- Custom player nicknames (validated for uniqueness and letters-only)
- Custom symbol selection per player (`X` or `O`, no duplicates)
- Colorful, boxed board rendered with `rich` (`Panel` + `Table`)
- Win and draw detection across all rows, columns, and diagonals
- Animated ASCII-art banner for the winner
- Restart or quit menu after each round
- Input validation throughout (names, symbols, move positions)

## Requirements

- Python 3.x
- `rich`
- `pyfiglet`

## Installation

```bash
pip install rich pyfiglet
```

## Usage

```bash
python main.py
```

## How to Play

1. From the start menu, choose **1** to start a new game (or **2** to quit).
2. Each player enters a nickname (letters only, must be unique between players).
3. Each player picks a symbol, **X** or **O** (each symbol can only be claimed once).
4. Players take turns entering a number from **1–9**, matching the board position they want to play.
5. The game detects a win (any full row, column, or diagonal) and displays the winner's name in a stylized banner, or announces a draw if the board fills up with no winner.
6. At the end of a round, choose to start a **new game** or **quit**.

## Board Layout Reference

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```
Enter the number shown to place your symbol in that cell.

## Project Structure

Everything lives in `main.py`:

| Class    | Responsibility                                              |
|----------|---------------------------------------------------------------|
| `Player` | Collects and validates a player's name and symbol             |
| `Menu`   | Displays the start menu, win banner, and end-of-round menu     |
| `Board`  | Holds board state, renders it, and validates/applies moves     |
| `Game`   | Runs the main game loop, checks for wins/draws, and orchestrates play |

## Notes

- Names must contain letters only and be unique across both players.
- Symbol input is case-insensitive (converted to uppercase automatically) and must be either `X` or `O`.
