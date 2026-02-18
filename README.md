# Go Game

A Python implementation of the classic board game **Go**.

> **Author:** Pedro Jerónimo  
> **GitHub:** [github.com/pedrojeronim0](https://github.com/pedrojeronim0)

---

## About the Game

Go is an abstract strategy board game for two players. Players alternate placing stones of their colour on the board, aiming to form territories around empty regions. The player with the highest score wins — score is calculated by the number of intersections occupied by a player's stones plus the intersections forming territories bordered exclusively by that player's stones.

The game ends when both players pass consecutively.

**Illegal moves:**
- **Suicide** — a move is illegal if it leaves one or more of the player's own stones with no liberties after the move is resolved.
- **Repetition (Ko)** — a move is illegal if it recreates a board state that occurred earlier in the game.

---

## Project Structure

The implementation is contained in a single file: `FP2324P2.py`

It defines three **Abstract Data Types (ADTs)** and a set of additional functions:

### ADT: Intersection
Represents a board intersection identified by a column (`A`–`S`) and a row (`1`–`19`).

| Function | Description |
|---|---|
| `create_intersection(column, row)` | Creates an intersection |
| `get_col(intersection)` | Returns the column |
| `get_row(intersection)` | Returns the row |
| `is_intersection(arg)` | Checks if argument is a valid intersection |
| `intersections_equal(i1, i2)` | Checks if two intersections are equal |
| `intersections_repeated(intersections)` | Checks for repeated intersections in a tuple |
| `intersection_to_str(intersection)` | Returns string representation (e.g. `'B13'`) |
| `str_to_intersection(text)` | Returns intersection from string |
| `get_adjacent_intersections(intersection, l)` | Returns adjacent intersections in reading order |
| `sort_intersections(intersections)` | Sorts intersections in reading order |

### ADT: Stone
Represents a Go stone — white (`'O'`), black (`'X'`), or neutral (`'.'`).

| Function | Description |
|---|---|
| `create_white_stone()` | Creates a white stone |
| `create_black_stone()` | Creates a black stone |
| `create_neutral_stone()` | Creates a neutral stone |
| `is_stone(arg)` | Checks if argument is a valid stone |
| `is_white_stone(stone)` | Checks if stone belongs to the white player |
| `is_black_stone(stone)` | Checks if stone belongs to the black player |
| `is_player_stone(stone)` | Checks if stone belongs to any player |
| `stones_equal(s1, s2)` | Checks if two stones are equal |
| `stone_to_str(stone)` | Returns string representation |

### ADT: Goban
Represents the Go board and the stones placed on it. Supports sizes 9×9, 13×13, and 19×19.

| Function | Description |
|---|---|
| `create_empty_goban(n)` | Creates an empty n×n goban |
| `create_goban(n, white_ints, black_ints)` | Creates a goban with stones placed |
| `copy_goban(goban)` | Returns a copy of a goban |
| `get_last_intersection(goban)` | Returns the top-right intersection |
| `get_stone(goban, intersection)` | Returns the stone at an intersection |
| `get_chain(goban, intersection)` | Returns the chain passing through an intersection |
| `place_stone(goban, intersection, stone)` | Places a stone on the goban |
| `remove_stone(goban, intersection)` | Removes a stone from the goban |
| `remove_chain(goban, intersections_tuple)` | Removes all stones in a chain |
| `is_goban(arg)` | Checks if argument is a valid goban |
| `is_valid_intersection(goban, intersection)` | Checks if an intersection is valid within the goban |
| `gobans_equal(g1, g2)` | Checks if two gobans are equal |
| `goban_to_str(goban)` | Returns string representation of the goban |
| `get_intersections(goban, stone)` | Returns all intersections occupied by a given stone |
| `get_territories(goban)` | Returns all territories of the goban |
| `get_different_adjacents(goban, intersections)` | Returns adjacent intersections of a different occupation state |
| `make_move(goban, intersection, stone)` | Performs a move and captures opponent's stones with no liberties |
| `get_player_stones(goban)` | Returns the count of stones for each player |

### Additional Functions

| Function | Description |
|---|---|
| `calculate_scores(goban)` | Returns the score `(white, black)` |
| `is_legal_move(goban, intersection, stone, previous_goban)` | Checks if a move is legal (no suicide, no Ko) |
| `player_turn(goban, stone, previous_goban)` | Handles a player's turn; returns `False` if the player passes |
| `go(n, white_stones, black_stones)` | Runs a full two-player Go game; returns `True` if white wins |

---

## How to Play

Run the following in your terminal:

```bash
python3 -c "from FP2324P2 import *; go(9, (), ())"
```

Or launch an interactive Python session:

```bash
python3
```

```python
>>> from FP2324P2 import *

# Start a 9x9 game with an empty board
>>> go(9, (), ())

# Start a game with pre-placed stones
>>> ib = ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3')
>>> ip = ('E4', 'E5', 'F4', 'F5', 'G6', 'G7')
>>> go(9, ib, ip)
```

During the game, each player is prompted to either enter an intersection (e.g. `G5`) or `P` to pass. The game ends when both players pass consecutively.

---

## Requirements

- Python 3 (no external libraries required)
