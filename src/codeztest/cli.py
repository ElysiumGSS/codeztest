"""Command line interface for codeztest."""

import argparse
from . import hello


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="codeztest CLI")
    parser.add_argument("name", nargs="?", default="world", help="Name to greet")
    args = parser.parse_args(argv)
    print(hello(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
