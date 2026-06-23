
---

# Text Normalization and Information Retrieval on Historical German Texts

## Project Overview
This project investigates the impact of text normalization on information retrieval (IR) performance using historical German newspaper texts.

We compare retrieval effectiveness between:
- original historical text
- normalized / linguistically processed text

The goal is to evaluate whether normalization improves retrieval quality in non-standardized historical language data.

---

## Research Question
How does text normalization affect information retrieval performance on historical German newspaper texts?

---

## Data
We use a subset of the Deutsches Textarchiv (DTA), a historical German corpus.

The corpus contains historical German newspaper texts with multiple linguistic layers, including original orthography and normalized/lemmatized forms.

---

## Methods

### Retrieval Models
- TF-IDF (baseline model)
- BM25 (optional extension)

### Text Processing
- Tokenization
- Optional normalization (historical spelling variation handling)
- Lemmatization (if available from corpus)

### Evaluation
- Precision@k
- Recall@k
- Mean Average Precision (MAP)
- Mean Reciprocal Rank (MRR)

---

## Project Structure

```text
src/        Core implementation (retrieval, normalization, evaluation)
data/       Dataset and corpus files
notebooks/  Experimental analysis and visualization
results/    Output files, tables, figures
scripts/    Utility scripts
````

---

## How to Run

### 1. Run retrieval pipeline

```bash
python src/retrieval.py
```

### 2. Or use Jupyter notebooks

```bash
jupyter notebook notebooks/01_experiments.ipynb
```

---

## Team & Contributions

* Student A: Data processing, corpus preparation, text normalization
* Student B: Retrieval models, evaluation pipeline, experimental analysis
* Joint Work: Research design, query set creation, result interpretation

---

## Current Status

* Project structure initialized ✔
* Dataset selected ✔
* Baseline retrieval in progress ⏳
* Evaluation pipeline under development ⏳

---

## Notes

This project is part of a seminar on Text Similarity and Information Retrieval at the University of Stuttgart.

```

---
