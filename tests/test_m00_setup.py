"""Milestone 0: your tools are set up. Run: pytest tests/test_m00_setup.py"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_python_is_3_10_or_newer():
    assert sys.version_info >= (3, 10), f"You have Python {sys.version.split()[0]}; install 3.10 or newer"


def test_running_inside_a_virtual_environment():
    assert sys.prefix != sys.base_prefix, (
        "Activate your virtual environment first: "
        ".venv\\Scripts\\activate on Windows, source .venv/bin/activate on Mac/Linux"
    )


def test_gitignore_keeps_secrets_and_clutter_out():
    gitignore = ROOT / ".gitignore"
    assert gitignore.exists(), "Create a file called .gitignore in the project folder"
    text = gitignore.read_text(encoding="utf-8")
    for entry in [".venv", ".env", "__pycache__"]:
        assert entry in text, f"Add a line '{entry}' to .gitignore"


def test_the_handbook_is_in_data():
    assert len(list((ROOT / "data").glob("*.md"))) >= 5, "The data folder should hold the handbook files"
