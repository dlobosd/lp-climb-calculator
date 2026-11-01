# LP Climb Calculator

A tiny Python CLI that estimates how many ranked games you need to reach an LP target.

## Run

Requires Python 3.10+ and no third-party packages.

```bash
python lp_calculator.py --current 500 --target 600 --win-rate 60
# Estimated games: 25
```

Optional flags: `--gain 20 --loss 20`. Win rate is a percentage (0 to 100).

The calculation uses expected LP per game:
`win_rate * gain - (1 - win_rate) * loss`.
If expected progress is zero or negative, the tool reports that the target
cannot be estimated with positive progress.

This is a rough planning estimate, not a prediction of your first arrival at
the target. LP gains, demotions, streaks and moving rank cutoffs are not modeled.

## Tests

```bash
python -m unittest discover -v
```
