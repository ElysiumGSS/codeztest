"""Allow running `python -m codeztest`."""
from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
