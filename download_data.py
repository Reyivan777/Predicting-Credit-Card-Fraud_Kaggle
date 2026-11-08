from pathlib import Path

import kagglehub


def main():
    output_dir = Path(__file__).resolve().parent / "data"
    expected_files = ("train.csv", "test.csv", "sample_submission.csv")
    if all((output_dir / name).is_file() and (output_dir / name).stat().st_size > 0 for name in expected_files):
        print("Competition files already exist:", output_dir)
        return
    path = kagglehub.competition_download(
        "playground-series-s6e11",
        output_dir=str(output_dir),
    )
    print("Path to competition files:", path)


if __name__ == "__main__":
    main()
