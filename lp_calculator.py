"""Estimate ranked games from constant LP gains, losses and win rate."""
import argparse
import math


def estimate_games(current, target, win_rate, gain=20, loss=20):
    """Return expected games, or None when expected progress is nonpositive."""
    if not all(math.isfinite(v) for v in (current, target, win_rate, gain, loss)):
        raise ValueError("All inputs must be finite.")
    if not 0 <= win_rate <= 1:
        raise ValueError("Win rate must be between 0 and 1.")
    if gain <= 0 or loss <= 0:
        raise ValueError("LP gain and loss must be positive.")
    if current >= target:
        return 0
    progress = win_rate * gain - (1 - win_rate) * loss
    if progress <= 0:
        return None
    return math.ceil((target - current) / progress)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current", type=float, required=True)
    parser.add_argument("--target", type=float, required=True)
    parser.add_argument("--win-rate", type=float, required=True,
                        help="Win percentage, for example 60")
    parser.add_argument("--gain", type=float, default=20)
    parser.add_argument("--loss", type=float, default=20)
    args = parser.parse_args()
    try:
        games = estimate_games(args.current, args.target, args.win_rate / 100,
                               args.gain, args.loss)
    except ValueError as error:
        parser.error(str(error))
    if games is None:
        print("No positive expected LP progress with these settings.")
    elif games == 0:
        print("Target already reached!")
    else:
        print(f"Estimated games: {games}")
    print("Rough estimate only: fixed LP values, no demotions or changing cutoffs.")


if __name__ == "__main__":
    main()
