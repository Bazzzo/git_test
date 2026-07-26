#!/usr/bin/env python3
"""Convert text into a stable lowercase hyphen-separated identifier."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata

_NON_ALPHANUMERIC = re.compile(r"[^a-z0-9]+")


def normalise(text: str) -> str:
    """Return a deterministic ASCII identifier for *text*."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return _NON_ALPHANUMERIC.sub("-", ascii_text.lower()).strip("-")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert text into a lowercase hyphen-separated identifier."
    )
    parser.add_argument("text", help="text to normalise")
    args = parser.parse_args(argv)

    result = normalise(args.text)
    if not result:
        print("error: normalisation produced an empty result", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
