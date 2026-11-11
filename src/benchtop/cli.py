"""Benchtop command-line interface."""

import argparse
import sys
from pathlib import Path


def ingest(file: Path) -> None:
    """Ingest an instrument file and convert it to a better format."""
    if not file.exists():
        print(f"Error: file not found: {file}", file=sys.stderr)
        sys.exit(1)
    print(f"Ingesting {file}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="benchtop",
        description="CLI tools to convert instrument files to better formats.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest", help="Ingest an instrument file.")
    ingest_parser.add_argument("file", type=Path, help="Path to the instrument file.")

    args = parser.parse_args()

    if args.command == "ingest":
        ingest(args.file)


if __name__ == "__main__":
    main()
