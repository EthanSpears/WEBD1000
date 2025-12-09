
#!/usr/bin/env python3
import random
import time
import math
from collections import Counter
from typing import List, Dict, Tuple, Optional

# -------------------------------
# Configuration (Friendly UX)
# -------------------------------
USE_DELAYS = True
DELAY = 0.3

def pause():
    if USE_DELAYS:
        time.sleep(DELAY)

def sep(char: str = "-", width: int = 50):
    print(char * width)


# Expanded move set (includes lizard & spock)
valid_moves: List[str] = ["rock", "paper", "scissors", "lizard", "spock"]
valid_set = set(valid_moves)

# Scoreboard accumulates across matches
score: Dict[str, int] = {"player": 0, "cpu": 0, "ties": 0}

# History of all rounds (across all matches)
# Each record: {"round": int, "player": str, "cpu": str, "result": "player|cpu|tie"}
history: List[Dict[str, object]] = []


# For RPSLS (Rock Paper Scissors Lizard Spock)
wins_over: set[Tuple[str, str]] = {
    ("rock", "scissors"), ("rock", "lizard"),
    ("paper", "rock"), ("paper", "spock"),
    ("scissors", "paper"), ("scissors", "lizard"),
    ("lizard", "spock"), ("lizard", "paper"),
    ("spock", "scissors"), ("spock", "rock"),
}


# -------------------------------
# Part A — Functions
# -------------------------------
def get_player_move(valid_set: set[str]) -> str:
    """
    Prompt user for a move, sanitize to lowercase, and loop until valid.
    Accepts full words only to avoid ambiguity with 'scissors' vs 'spock'.
    """
    while True:
        user_in = input("Your move (rock/paper/scissors/lizard/spock): ").strip().lower()
        if user_in in valid_set:
            return user_in
        print("Invalid move. Please type one of:", ", ".join(sorted(valid_set)))


def get_cpu_move(valid_moves: List[str]) -> str:
    """Random choice from valid_moves."""
    return random.choice(valid_moves)


def decide_winner(player: str, cpu: str) -> str:
    """Return 'player' | 'cpu' | 'tie' based on wins_over rules."""
    if player == cpu:
        return "tie"
    elif (player, cpu) in wins_over:
        return "player"
    elif (cpu, player) in wins_over:
        return "cpu"
    else:
        # Should never happen if inputs are validated
        return "tie"


def print_scoreboard(score: Dict[str, int]) -> None:
    """Pretty-print the cumulative scoreboard."""
    sep("=")
    print("SCOREBOARD")
    sep("=")
    print(f"PLAYER WINS : {score['player']}")
    print(f"CPU    WINS : {score['cpu']}")
    print(f"TIES        : {score['ties']}")
    sep("=")


def print_history(history_list: List[Dict[str, object]], last_n: Optional[int] = None) -> None:
    """
    Print last N rounds or all if last_n is None.
    """
    sep()
    print("ROUND HISTORY")
    sep()
    items = history_list if last_n is None else history_list[-last_n:]
    if not items:
        print("No rounds played yet.")
        sep()
        return

    for h in items:
        r = h.get("round")
        p = h.get("player")
        c = h.get("cpu")
        res = h.get("result")
        print(f"Round {r:>3}: Player={p:<8} CPU={c:<8} Result={res}")
    sep()


# -------------------------------
# Part B — Integration Enhancements
# - Streak tracker
# - Simple analytics
# - Friendly UX
# -------------------------------
def compute_analytics(history_list: List[Dict[str, object]]) -> Dict[str, object]:
    """
    Compute simple analytics from the entire history:
    - most used move by player
    - most used move by CPU
    """
    player_moves = [h["player"] for h in history_list]
    cpu_moves = [h["cpu"] for h in history_list]
    pm = Counter(player_moves)
    cm = Counter(cpu_moves)
    most_player = pm.most_common(1)[0][0] if pm else None
    most_cpu = cm.most_common(1)[0][0] if cm else None
    return {
        "player_most_used": most_player,
        "cpu_most_used": most_cpu,
        "player_counts": dict(pm),
        "cpu_counts": dict(cm),
    }


def get_best_of() -> int:
    """
    Ask for best-of-N (odd only; validate).
    Returns a positive odd integer.
    """
    while True:
        try:
            n_str = input("Best-of-N (odd number, e.g., 3, 5, 7): ").strip()
            n = int(n_str)
            if n > 0 and n % 2 == 1:
                return n
            print("Please enter a positive odd number.")
        except ValueError:
            print("Invalid number. Try again.")


def play_match(match_no: int) -> None:
    """
    Play one best-of-N match, update cumulative scoreboard and append history entries.
    Tracks max consecutive wins (streaks) for both sides within the match.
    """
    sep("=")
    print(f"START MATCH #{match_no}")
    sep("=")

    best_of = get_best_of()
    needed_wins = math.ceil(best_of / 2)

    # Per-match counters for determining match winner
    player_wins_this_match = 0
    cpu_wins_this_match = 0

    # Streaks (per match)
    player_current_streak = 0
    player_max_streak = 0
    cpu_current_streak = 0
    cpu_max_streak = 0

    round_no = len(history) + 1  # continue numbering across all matches

    while player_wins_this_match < needed_wins and cpu_wins_this_match < needed_wins:
        print()
        sep()
        print(f"ROUND {round_no}")
        sep()

        player_move = get_player_move(valid_set)
        cpu_move = get_cpu_move(valid_moves)

        pause()
        print(f"CPU chose: {cpu_move}")
        pause()

        result = decide_winner(player_move, cpu_move)
        if result == "player":
            print("🎉 PLAYER wins the round!")
            score["player"] += 1
            player_wins_this_match += 1
            player_current_streak += 1
            cpu_current_streak = 0
            player_max_streak = max(player_max_streak, player_current_streak)
        elif result == "cpu":
            print("🤖 CPU wins the round!")
            score["cpu"] += 1
            cpu_wins_this_match += 1
            cpu_current_streak += 1
            player_current_streak = 0
            cpu_max_streak = max(cpu_max_streak, cpu_current_streak)
        else:
            print("⏸️ It's a tie.")
            score["ties"] += 1
            # ties break streaks (no one continues)
            player_current_streak = 0
            cpu_current_streak = 0

        # Record round
        history.append({
            "round": round_no,
            "player": player_move,
            "cpu": cpu_move,
            "result": result
        })

        round_no += 1

    # Match complete
    pause()
    sep("=")
    if player_wins_this_match > cpu_wins_this_match:
        print("✅ MATCH RESULT: PLAYER wins the match!")
    else:
        print("✅ MATCH RESULT: CPU wins the match!")
    sep("=")

    # Show per-match streaks
    print(f"PLAYER max consecutive wins this match: {player_max_streak}")
    print(f"CPU    max consecutive wins this match: {cpu_max_streak}")

    # Print cumulative scoreboard
    print_scoreboard(score)

    # Simple analytics (from entire history)
    analytics = compute_analytics(history)
    print("ANALYTICS (from all rounds so far)")
    sep()
    if analytics["player_most_used"] is None:
        print("No data yet.")
    else:
        print(f"Player most-used move: {analytics['player_most_used']}")
        print(f"CPU most-used move   : {analytics['cpu_most_used']}")
        print("Move counts (player):", analytics["player_counts"])
        print("Move counts (cpu)   :", analytics["cpu_counts"])
    sep()


def main():
    print()
    sep("=")
    print("ROCK PAPER SCISSORS LIZARD SPOCK")
    sep("=")
    print("Rules:")
    print(" - Rock crushes Scissors & Lizard")
    print(" - Paper covers Rock & disproves Spock")
    print(" - Scissors cut Paper & decapitate Lizard")
    print(" - Lizard poisons Spock & eats Paper")
    print(" - Spock smashes Scissors & vaporizes Rock")
    sep()

    match_no = 1
    while True:
        play_match(match_no)
        match_no += 1

        # Optionally play again
        ans = input("Play another match? (y/n): ").strip().lower()
        if ans not in ("y", "yes"):
            break

    print_history(history)  # Show full history at the end
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    main()
