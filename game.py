import random
from typing import Dict

# ---------------- GAME STATE ----------------

GameState = Dict[str, object]

def initial_game_state() -> GameState:
    return {
        "round": 1,
        "max_rounds": 3,
        "user_score": 0,
        "bot_score": 0,
        "user_bomb_used": False,
        "bot_bomb_used": False,
    }

# ---------------- RULES ----------------

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

RPS_WINS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

# ---------------- LOGIC (TOOLS STYLE) ----------------

def validate_move(move: str, bomb_used: bool) -> Dict:
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "INVALID_MOVE"}

    if move == "bomb" and bomb_used:
        return {"valid": False, "reason": "BOMB_ALREADY_USED"}

    return {"valid": True, "move": move}

def resolve_round(user_move: str, bot_move: str) -> Dict:
    # Draws
    if user_move == bot_move:
        return {"winner": "draw", "reason_code": "SAME_MOVE"}

    if user_move == "bomb" and bot_move == "bomb":
        return {"winner": "draw", "reason_code": "BOMB_BOTH"}

    # Bomb rules
    if user_move == "bomb":
        return {"winner": "user", "reason_code": "BOMB_OVERRIDES"}

    if bot_move == "bomb":
        return {"winner": "bot", "reason_code": "BOMB_OVERRIDES"}

    # Standard RPS
    if RPS_WINS[user_move] == bot_move:
        return {"winner": "user", "reason_code": "RPS_STANDARD_RULE"}

    return {"winner": "bot", "reason_code": "RPS_STANDARD_RULE"}

def referee_explanation(user_move: str, bot_move: str, winner: str) -> str:
    if winner == "draw":
        return f"Both played {user_move}. It's a draw."

    if user_move == "bomb":
        return f"You used bomb. Bomb beats {bot_move}."

    if bot_move == "bomb":
        return f"Bot used bomb. Bomb beats {user_move}."

    if winner == "user":
        return f"{user_move.capitalize()} beats {bot_move}."

    return f"{bot_move.capitalize()} beats {user_move}."

# ---------------- GAME LOOP (CHATBOT) ----------------

def run_game():
    state = initial_game_state()

    print("Welcome to Rock–Paper–Scissors–Plus")
    print("Referee Rules:")
    print("- Best of 3 rounds")
    print("- Moves: rock, paper, scissors, bomb")
    print("- Bomb can be used once per game")
    print("- Bomb beats everything, bomb vs bomb is draw")
    print("- Invalid input wastes the round\n")

    while state["round"] <= state["max_rounds"]:
        user_input = input(
            f"Referee (Round {state['round']}): "
            "Make your move → rock / paper / scissors / bomb: "
        )

        validation = validate_move(user_input, state["user_bomb_used"])

        # Bot move (respects bomb rule)
        bot_moves = ["rock", "paper", "scissors"]
        if not state["bot_bomb_used"]:
            bot_moves.append("bomb")
        bot_move = random.choice(bot_moves)

        # Invalid input → waste round
        if not validation["valid"]:
            print(
                f"\nReferee: Invalid move. Reason Code: {validation['reason']}"
                "\nThis round is wasted.\n"
            )
            state["round"] += 1
            continue

        user_move = validation["move"]

        # Track bomb usage
        if user_move == "bomb":
            state["user_bomb_used"] = True
        if bot_move == "bomb":
            state["bot_bomb_used"] = True

        result = resolve_round(user_move, bot_move)
        winner = result["winner"]
        reason_code = result["reason_code"]

        if winner == "user":
            state["user_score"] += 1
        elif winner == "bot":
            state["bot_score"] += 1

        explanation = referee_explanation(user_move, bot_move, winner)

        print(f"\nReferee: You played → {user_move}")
        print(f"Referee: Bot played → {bot_move}")
        print(f"Referee Decision: {explanation}")
        print(f"Reason Code: {reason_code}")
        print(
            f"Score → You: {state['user_score']} | "
            f"Bot: {state['bot_score']}\n"
        )

        state["round"] += 1

    print("\nReferee: Game over. Final result:")
    if state["user_score"] > state["bot_score"]:
        print("Winner: YOU 🎉")
    elif state["bot_score"] > state["user_score"]:
        print("Winner: BOT 🤖")
    else:
        print("Result: DRAW")

# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    run_game()
