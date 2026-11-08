"""Download the original competition files from Kaggle.

Run from the repository root:
    python download_data.py
"""

from pathlib import Path

import kagglehub

COMPETITION = "playground-series-s6e11"
DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = kagglehub.competition_download(
        COMPETITION,
        output_dir=str(DATA_DIR),
    )
    print(f"Competition data downloaded to: {path}")
    for filename in ("train.csv", "test.csv", "sample_submission.csv"):
        file_path = DATA_DIR / filename
        print(f"{filename}: {'found' if file_path.is_file() else 'not found'}")


if __name__ == "__main__":
    main()
