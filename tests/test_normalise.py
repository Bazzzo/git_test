import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "normalise.py"
sys.path.insert(0, str(ROOT))

from normalise import normalise


class NormaliseTests(unittest.TestCase):
    def test_acceptance_examples(self) -> None:
        examples = {
            "Hello, World!": "hello-world",
            "  Multiple   spaces  ": "multiple-spaces",
            "Crème brûlée": "creme-brulee",
            "already-clean": "already-clean",
        }
        for source, expected in examples.items():
            with self.subTest(source=source):
                self.assertEqual(normalise(source), expected)

    def test_cli_success_prints_only_identifier(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CLI), "Hello, World!"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "hello-world\n")
        self.assertEqual(result.stderr, "")

    def test_cli_rejects_empty_result(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CLI), "***"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("empty result", result.stderr)


if __name__ == "__main__":
    unittest.main()
