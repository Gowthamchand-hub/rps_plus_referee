#AI Game Referee – Rock Paper Scissors Plus

__Overview__

This project is a simple AI referee chatbot that runs a short game of
Rock–Paper–Scissors–Plus between a user and the bot.
The referee is responsible for enforcing the rules, tracking the game state,
and clearly explaining the outcome of each round.

The goal of this assignment was not to build a fancy UI, but to focus on
correct logic, clean structure, and clarity in how decisions are made and
communicated.

__Game Rules__

-The game is played as best of 3 rounds
-Valid moves are: rock, paper, scissors, and bomb
-Each player can use bomb only once per game
-Bomb vs bomb results in a draw
-Invalid input wastes the round
-The game ends automatically after 3 rounds

__State Model__

The game uses an explicit state object to keep track of everything needed to
run the game correctly, including:

-Current round number
-Maximum number of rounds
-User score
-Bot score
-Whether the bomb has already been used by each player

All state is stored in a Python dictionary and passed through the game loop.
Nothing is stored implicitly in prompts or hidden memory.
This makes the behavior deterministic, easier to debug, and easy to reason
about.

__Game Logic Design__

The implementation is intentionally split into clear responsibilities:

-Input validation checks whether a move is valid and whether bomb usage
follows the rules.
-Round resolution applies the game rules to determine the winner.
-State updates handle score changes, bomb usage, and round progression.
-Response generation explains the outcome in a referee-style, human-readable
way.

Keeping these concerns separate makes the code easier to maintain and extend.

__Decision Reason Codes__

In addition to human-readable explanations, each round outcome also includes a
machine-readable reason code (for example: RPS_STANDARD_RULE,
BOMB_OVERRIDES, SAME_MOVE).

This allows decisions to be:

-Audited or logged easily
-Debugged without relying only on text output
-Extended later for UI, analytics, or replay features

The idea was to separate why a decision happened from how it is explained
to the user.

__Agent Design__

The referee is designed as a single agent that:

-Interprets user input
-Applies deterministic game logic through small, focused functions
-Maintains explicit game state outside of prompts
-Communicates decisions conversationally

Although the implementation uses plain Python, the structure follows
agent-oriented design principles and can be easily adapted to an Agent
Development Kit (ADK) style setup if needed.

__Execution Model__

The game runs in a simple command-line conversational loop:

-The referee explains the rules.
-The user is prompted for a move.
-The bot selects a valid move.
-The referee resolves the round and explains the decision.
-Scores are updated and displayed.
-The game ends automatically after three rounds.

No databases, external APIs, or UI frameworks are used.

__Tradeoffs__

-A CLI-based interface was chosen to keep the focus on logic and state handling.
-The bot uses random move selection rather than strategy to keep the behavior
simple and predictable.

__Future Improvements__

With more time, this could be extended to include:

-Multiple agents (for example, a referee agent and a strategy agent)
-A full round-by-round game transcript or replay mode
-A simple UI or web interface
-A smarter bot that adapts based on previous rounds

## How to Run
```bash
python game.py
