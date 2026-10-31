import sys
from pathlib import Path

# Agar bisa dijalankan dari mana saja (python src/code05_proyek1/main.py maupun python -m code05_proyek1.main)
_SRC = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, _SRC)

from code05_proyek1.application import AnomalyApplication  # noqa: E402


def main() -> None:
    AnomalyApplication().run()


if __name__ == "__main__":
    main()
