# Historische Textnormalisierung und Anfragegenerierung für Information Retrieval

## Projektübersicht

Dieses Projekt untersucht, wie sich die automatische Normalisierung historischer deutscher Texte auf die Qualität von LLM-generierten Suchanfragen sowie auf die Retrieval-Performance auswirkt.

Das Projekt ist Teil des Seminars **Text Similarity: From Lexical Measures to Neural Models** an der Universität Stuttgart.

Im Mittelpunkt stehen zwei komplementäre Forschungsfragen:

1. **Textnormalisierung**
2. **LLM-basierte Anfragegenerierung**

Die erzeugten Suchanfragen werden anschließend im Rahmen eines Information-Retrieval-Experiments evaluiert.

---

## Forschungsfragen

### RQ1 – Textnormalisierung

Verbessert die automatische Normalisierung historischer deutscher Texte die Retrieval-Performance?

Verglichen werden folgende Textversionen:

- historischer Originaltext
- automatisch normalisierter Text (z. B. mit TransNorma oder einem LLM)
- DTA-standardisierter Text

---

### RQ2 – Anfragegenerierung

Welchen Einfluss haben unterschiedliche Prompting-Strategien auf die Qualität automatisch generierter Suchanfragen?

Verglichen werden:

- Standard Prompting
- Summarize-then-Ask (SAP)

---

## Hypothese

Die automatische Normalisierung historischer deutscher Texte verbessert die Qualität von LLM-generierten Suchanfragen und führt dadurch zu einer besseren Retrieval-Performance.

Darüber hinaus wird erwartet, dass unterschiedliche Prompting-Strategien messbare Unterschiede hinsichtlich der Retrieval-Effektivität erzeugen.

---

# Datensatz

**Quelle**

Deutsches Textarchiv (DTA)

**Ausgewählter Themenbereich**

Historiographie

**Zusammensetzung des Datensatzes**

- **30 Dokumente aus dem Bereich Historiographie**
  - dienen als Grundlage für die Anfragegenerierung
  - bilden die relevanten Dokumente für die Evaluation

- **70 weitere Dokumente**
  - zufällig aus anderen DTA-Fachbereichen ausgewählt
  - dienen als Distraktoren während des Retrievals

Jede generierte Suchanfrage besitzt genau ein relevantes Dokument, aus dem sie erzeugt wurde.

---

# Methodik

## 1. Anfragegenerierung

Für die 30 Historiographie-Dokumente werden automatisch Suchanfragen mithilfe zweier Prompting-Strategien generiert.

Verglichen werden:

- Standard Prompting
- Summarize-then-Ask (SAP)

Aus jedem Dokument wird eine Suchanfrage erzeugt.

---

## 2. Textnormalisierung

Die ursprünglichen historischen Dokumente werden automatisch normalisiert.

Verglichen werden:

- Originaltext
- automatisch normalisierte Version
- DTA-standardisierte Version

Die generierten Suchanfragen bleiben unverändert. Lediglich die Dokumentrepräsentation wird verändert.

---

## 3. Information Retrieval

Das Retrieval wird mit einem einzelnen Retrieval-Modell durchgeführt (z. B. TF-IDF oder BM25).

Für jede Suchanfrage wird sowohl auf

- dem Originalkorpus
- als auch auf dem normalisierten Korpus

recherchiert und die resultierenden Rankings werden miteinander verglichen.

---

# Evaluation

## Quantitative Evaluation

Die Retrieval-Performance wird anhand etablierter IR-Metriken bewertet:

- Recall@1
- Recall@5
- Recall@10
- Mean Reciprocal Rank (MRR)
- nDCG@10 (optional)

Als relevantes Dokument gilt jeweils das Dokument, aus dem die entsprechende Suchanfrage generiert wurde.

## Qualitative Evaluation

Zusätzlich werden ausgewählte Beispiele manuell analysiert, um

- Unterschiede zwischen Original- und normalisierten Texten,
- Unterschiede zwischen den generierten Suchanfragen sowie
- deren Auswirkungen auf das Retrieval

zu untersuchen.

---

# Projektpipeline

```text
30 Historiographie-Dokumente
              │
              ├──────────────► Anfragegenerierung
              │                (Standard Prompt / SAP)
              │
              ▼
      Originaldokumente
              │
              ▼
     Automatische Normalisierung
              │
              ▼
     Normalisierte Dokumente
              │
              ▼
      Information Retrieval
        (TF-IDF / BM25)
              │
              ▼
          Evaluation
```

---

# Projektstruktur

```
project/

├── data/
│   ├── original/
│   ├── normalized/
│   ├── queries/
│   └── retrieval/
│
├── notebooks/
│
├── src/
│   ├── normalization/
│   ├── query_generation/
│   ├── retrieval/
│   └── evaluation/
│
├── results/
│
└── README.md
```

---

# Team

### Shujing Li

- Textnormalisierung
- Evaluation der Retrieval-Ergebnisse

### Emma Hermann

- Anfragegenerierung
- Prompt Engineering

Gemeinsam:

- Experimentdesign
- Analyse der Ergebnisse
- Abschlussbericht

---

# Literatur

## Textnormalisierung

- Ehrmanntraut, A. (2025). *Historical German Text Normalization Using Type- and Token-Based Language Modeling.*
- Bollmann, M. (2012). *(Semi-)Automatic Normalization of Historical Texts using Distance Measures and the Norma Tool.*

## Anfragegenerierung

- Dai, Z., et al. (2022). *Promptagator: Few-shot Dense Retrieval from 8 Examples.*
- Thakur, N., et al. (2024). *SWIM-IR: Leveraging LLMs for Synthesizing Training Data Across Many Languages in Multilingual Dense Retrieval.*

## Datengrundlage

- Deutsches Textarchiv (DTA). https://www.deutschestextarchiv.de/
