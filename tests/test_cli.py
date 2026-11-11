"""Tests for the CLI."""

import subprocess
import sys
from pathlib import Path

import pytest


def run_benchtop(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "benchtop.cli", *args],
        capture_output=True,
        text=True,
    )


def test_ingest_file(tmp_path: Path) -> None:
    f = tmp_path / "sample.txt"
    f.write_text("data")
    result = run_benchtop("ingest", str(f))
    assert result.returncode == 0
    assert "Ingesting" in result.stdout


def test_ingest_missing_file(tmp_path: Path) -> None:
    result = run_benchtop("ingest", str(tmp_path / "missing.txt"))
    assert result.returncode != 0
    assert "Error" in result.stderr
