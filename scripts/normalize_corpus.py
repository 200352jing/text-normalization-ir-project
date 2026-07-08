from pathlib import Path

import spacy
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "ybracke/transnormer-19c-beta-v02"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "data" / "original"
OUTPUT_DIR = PROJECT_ROOT / "data" / "normalized_transnormer"

# Zum Testen: 100
# Für vollständige Normalisierung: None
TEST_LIMIT = 100

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def sentence_split(text: str) -> list[str]:
    """
    Sentence segmentation with spaCy sentencizer.
    This is more stable than splitting only by punctuation.
    """
    nlp = spacy.blank("de")
    nlp.add_pipe("sentencizer")

    # Increase max_length for long historical texts
    nlp.max_length = len(text) + 100

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    doc = nlp(text)

    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    return sentences


def normalize_sentence(sentence: str, tokenizer, model) -> str:
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

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def normalize_file(input_path: Path, output_path: Path, tokenizer, model) -> None:
    text = input_path.read_text(encoding="utf-8")
    sentences = sentence_split(text)

    if TEST_LIMIT is not None:
        sentences = sentences[:TEST_LIMIT]

    print(f"  Segments: {len(sentences)}")

    normalized_sentences = []

    for i, sentence in enumerate(sentences, start=1):
        print(f"  Segment {i}/{len(sentences)}")
        normalized_sentences.append(normalize_sentence(sentence, tokenizer, model))

    normalized_text = "\n".join(normalized_sentences)
    output_path.write_text(normalized_text, encoding="utf-8")


def main() -> None:
    files = [INPUT_DIR / "chladni_geschichtswissenschaft_1752.txt"]

    print(f"Loading model: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model.eval()

    for file_path in files:
        if not file_path.exists():
            print(f"File not found: {file_path}")
            continue

        print(f"\nNormalizing file: {file_path.name}")

        output_path = OUTPUT_DIR / file_path.name.replace(".txt", "_norm.txt")
        normalize_file(file_path, output_path, tokenizer, model)

        print(f"Saved: {output_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()