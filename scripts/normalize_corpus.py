from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "ybracke/transnormer-19c-beta-v02"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "data" / "original"
OUTPUT_DIR = PROJECT_ROOT / "data" / "normalized_transnormer"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def simple_sentence_split(text: str) -> list[str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    sentences = []
    for line in lines:
        parts = line.replace(". ", ".\n").replace("? ", "?\n").replace("! ", "!\n").split("\n")
        sentences.extend(part.strip() for part in parts if part.strip())

    return sentences


def normalize_text(text: str, tokenizer, model) -> str:
    sentences = simple_sentence_split(text)
    normalized_sentences = []
    sentences = sentences[:100]

    for i, sentence in enumerate(sentences, start=1):
        print(f"  Sentence {i}/{len(sentences)}")

        inputs = tokenizer(
            sentence,
            return_tensors="pt",
            truncation=True,
            max_length=512,
        )

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                num_beams=4,
                max_new_tokens=512,
            )

        normalized = tokenizer.decode(outputs[0], skip_special_tokens=True)
        normalized_sentences.append(normalized)

    return "\n".join(normalized_sentences)


def main() -> None:
    files = [INPUT_DIR / "chladni_geschichtswissenschaft_1752.txt"]

    if not files:
        print(f"No .txt files found in: {INPUT_DIR}")
        return

    print(f"Loading model: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model.eval()

    print(f"Found {len(files)} files.")

    for file_path in files:
        print(f"\nNormalizing file: {file_path.name}")

        text = file_path.read_text(encoding="utf-8")
        normalized_text = normalize_text(text, tokenizer, model)

        output_path = OUTPUT_DIR / file_path.name.replace(".txt", "_norm.txt")
        output_path.write_text(normalized_text, encoding="utf-8")

        print(f"Saved: {output_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()