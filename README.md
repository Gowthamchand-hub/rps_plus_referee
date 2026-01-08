# AI Game Referee – Rock Paper Scissors Plus

## Overview
This project implements a minimal AI referee chatbot that runs a short game of
Rock–Paper–Scissors–Plus between a user and the bot. The referee enforces rules,
tracks game state across rounds, and provides clear, round-by-round decisions.

The focus of this implementation is correctness, clarity of logic, and clean
separation of responsibilities rather than UI polish.

---

## Game Rules
- Best of 3 rounds
- Valid moves: rock, paper, scissors, bomb
- Bomb can be used only once per player per game
- Bomb beats all other moves
- Bomb vs bomb results in a draw
- Invalid input wastes the round
- Game ends automatically after 3 rounds

---

## State Model
The game uses an explicit state object to track:
- Current round number
- Maximum rounds
- User score
- Bot score
- Whether the bomb has been used by each player

State is stored in a Python dictionary and is not kept in prompts or implicit
agent memory. This ensures deterministic behavior and strict rule enforcement.

---

## Game Logic Design
The implementation separates concerns clearly:
- **Input validation** ensures moves are legal and bomb usage rules are respected.
- **Round resolution** determines the winner using explicit rules.
- **State updates** handle score changes, bomb usage, and round progression.
- **Response generation** explains each decision in a referee-style tone.

---

## Execution Model
The game runs in a simple command-line conversational loop:
1. The referee explains the rules.
2. The user is prompted for a move.
3. The bot selects a valid move.
4. The referee resolves the round and explains the outcome.
5. Scores are updated and displayed.
6. The game ends automatically after three rounds.

No databases, external APIs, or UI frameworks are used.

---

## Tradeoffs
- A CLI interface was chosen to keep the focus on logic and state management.
- The bot uses random move selection rather than strategy to keep behavior simple.

---

## Future Improvements
- Multi-agent setup (separate referee and strategist agents)
- Replay or audit mode using stored round history
- UI or web-based interface
- Smarter bot strategy based on game history

---

## How to Run
```bash
python game.py
