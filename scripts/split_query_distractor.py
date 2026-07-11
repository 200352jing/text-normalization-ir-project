from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

TOKEN_LIMIT = 512

FOLDER_CONFIGS = [
    {
        "input": DATA_DIR / "original",
        "first_part": DATA_DIR / "original_first_512",
        "remainder": DATA_DIR / "original_distractors",
    },
    {
        "input": DATA_DIR / "DTA_normalized",
        "first_part": DATA_DIR / "DTA_normalized_first_512",
        "remainder": DATA_DIR / "DTA_normalized_distractors",
    },
]


def split_file(
    input_path: Path,
    first_part_path: Path,
    remainder_path: Path,
    token_limit: int = TOKEN_LIMIT,
) -> tuple[int, int]:
    """
    Split a text file by whitespace-separated tokens.

    The first token_limit tokens are saved in first_part_path.
    All remaining tokens are saved in remainder_path.
    """
    text = input_path.read_text(encoding="utf-8")
    tokens = text.split()

    first_tokens = tokens[:token_limit]
    remaining_tokens = tokens[token_limit:]

    first_part_path.write_text(" ".join(first_tokens), encoding="utf-8")
    remainder_path.write_text(" ".join(remaining_tokens), encoding="utf-8")

    return len(first_tokens), len(remaining_tokens)


def process_folder(config: dict[str, Path]) -> None:
    input_dir = config["input"]
    first_part_dir = config["first_part"]
    remainder_dir = config["remainder"]

    first_part_dir.mkdir(parents=True, exist_ok=True)
    remainder_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("*.txt"))

    if not files:
        print(f"Keine TXT-Dateien gefunden in: {input_dir}")
        return

    print(f"\nVerarbeite {len(files)} Dateien aus: {input_dir.name}")

    for input_path in files:
        first_part_path = first_part_dir / input_path.name
        remainder_path = remainder_dir / input_path.name

        first_count, remainder_count = split_file(
            input_path=input_path,
            first_part_path=first_part_path,
            remainder_path=remainder_path,
        )

        print(
            f"{input_path.name}: "
            f"{first_count} Tokens gespeichert, "
            f"{remainder_count} Tokens als Rest"
        )


def main() -> None:
    for config in FOLDER_CONFIGS:
        process_folder(config)

    print("\nFertig.")


if __name__ == "__main__":
    main()