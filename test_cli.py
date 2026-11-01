"""Exercise the public command-line interface as a user would."""
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).with_name("lp_calculator.py")


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, check=False,
        )

    def test_estimate(self):
        result = self.run_cli("--current", "500", "--target", "600",
                              "--win-rate", "60")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Estimated games: 25", result.stdout)

    def test_nonpositive_progress(self):
        result = self.run_cli("--current", "500", "--target", "600",
                              "--win-rate", "50")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No positive expected LP progress", result.stdout)

    def test_invalid_percentage(self):
        result = self.run_cli("--current", "500", "--target", "600",
                              "--win-rate", "101")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Win rate must be between", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_required_arguments(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("required", result.stderr)


if __name__ == "__main__":
    unittest.main()
