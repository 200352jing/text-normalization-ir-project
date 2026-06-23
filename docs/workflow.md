
---

# Team Workflow (GitHub Collaboration)

## 1. Project Setup
We use a shared GitHub repository for all project work:
text-normalization-ir-project

The repository contains:
- code (src/)
- data (data/)
- experiments (notebooks/)
- results (results/)

---

## 2. General Working Principle
We work in a synchronized workflow to avoid conflicts and ensure reproducibility.

---

## 3. Before Starting Work
Always update your local repository:

```bash
git pull
````

This ensures you are working on the latest version of the project.

---

## 4. During Development

* Each team member works on their assigned module:

  * Student A: data preprocessing and text normalization
  * Student B: retrieval models and evaluation

* Avoid editing the same file simultaneously.

* Communicate before making structural changes.

---

## 5. After Completing Changes

Use the following Git workflow:

```bash
git add .
git commit -m "clear description of changes"
git push
```

---

## 6. Commit Message Rules

Good examples:

* "add TF-IDF baseline"
* "implement text normalization pipeline"
* "add evaluation metrics (MAP, MRR)"

Bad examples:

* "update"
* "fix"
* "changes"

---

## 7. Conflict Handling

If a merge conflict occurs:

1. Open the file with conflict markers:
   <<<<<<< HEAD
   ============

   > > > > > > > branch

2. Manually resolve the conflict

3. Then run:

```bash
git add .
git commit -m "resolve merge conflict"
git push
```

---

## 8. Communication Rules

* Discuss major changes before implementation
* Especially for:

  * dataset changes
  * evaluation design
  * project structure changes

---

## 9. Goal

Maintain a clean, reproducible, and collaborative workflow for a text similarity and information retrieval project.

```

---




