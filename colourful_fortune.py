#!/usr/bin/env python3

import subprocess
import sys

from lolpython import lol_py


def main() -> int:
    fortune_path = "@fortune@/bin/fortune"

    try:
        result = subprocess.run(
            [fortune_path],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"error: `fortune` failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode

    fortune_text = result.stdout.rstrip("\n")

    # Print the fortune in rainbow colors using lol-cat-py.
    lol_py(fortune_text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
